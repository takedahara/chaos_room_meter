import React from 'react';

interface ImageDisplayProps {
  imageUrl: string;
}

const ImageDisplay: React.FC<ImageDisplayProps> = ({ imageUrl }) => {
  return (
    <div>
      <img src={imageUrl} alt="Processed Image" />
    </div>
  );
};

export default ImageDisplay;






