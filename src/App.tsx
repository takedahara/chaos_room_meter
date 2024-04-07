import React from 'react';
import FileUpload from './FileUpload'; // FileUploadコンポーネントをインポート

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* FileUploadコンポーネントを呼び出す */}
        <FileUpload />
      </header>
    </div>
  );
}

export default App;

