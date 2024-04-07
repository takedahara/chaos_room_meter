const express = require('express');
const { spawn } = require('child_process');
const multer = require('multer');
const cors = require('cors');

const app = express();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
const upload = multer({ storage: storage });

app.use(cors());

app.get('/', (req, res) => {
  res.send('Welcome to the image processing server');
});

app.post('/process-image', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded');
  }

  const pythonProcess = spawn('python', ['analyze/obeya.py', req.file.path]);

  let data = '';

  pythonProcess.stdout.on('data', (chunk) => {
    data += chunk.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python script error: ${data}`);
    res.status(500).send('Internal Server Error');
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python script process exited with code ${code}`);
    try {
      const result = JSON.parse(data);
      res.json({ score: result.score }); // スコアをクライアントに送信
    } catch (error) {
      console.error(`Error parsing JSON: ${error}`);
      res.status(500).send('Internal Server Error');
    }
  });
});

const port = 3001;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});


