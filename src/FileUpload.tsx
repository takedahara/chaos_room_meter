import React, { useState } from 'react';

const FileUpload: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [score, setScore] = useState<number | null>(null); // スコアを保持するState
  const [error, setError] = useState<string | null>(null); // エラーメッセージを保持するState

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (files && files.length > 0) {
      setSelectedFile(files[0]);
    }
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('image', selectedFile);

      try {
        const response = await fetch('http://localhost:3001/process-image', {
          method: 'POST',
          body: formData
        });

        if (response.ok) {
          // JSON形式のレスポンスを取得
          const result = await response.json();
          // スコアをセット
          if (typeof result.score === 'number') {
            setScore(result.score);
          } else {
            setError('Invalid score received');
          }
        } else {
          setError('Error uploading image');
        }
      } catch (error: any) { // ここでerrorの型をanyにしています
        setError(error.message);
      }
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      {selectedFile && <p>Selected File: {selectedFile.name}</p>}
      <button onClick={handleUpload}>Upload</button>
      {score !== null && <p>Score: {score}</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
};

export default FileUpload;







