
import React, { useState } from 'react';
import axios from 'axios';

const ProvisionForm = () => {
  const [bucketName, setBucketName] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('Provisioning in progress...');

    try {
      const response = await axios.post('http://localhost:5000/provision', { bucketName });
      setStatus(response.data.message);
    } catch (error) {
      setStatus('Error during provisioning');
    }
  };

  return (
    <div>
      <h2>Provision AWS S3 Bucket</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter Bucket Name"
          value={bucketName}
          onChange={(e) => setBucketName(e.target.value)}
          required
        />
        <button type="submit">Provision</button>
      </form>
      <p>{status}</p>
    </div>
  );
};

export default ProvisionForm;
