import React, { useState, useEffect } from 'react';

function App() {
  const [prs, setPrs] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/prs')
      .then(res => res.json())
      .then(data => setPrs(data));
  }, []);

  const copyComment = (comment) => {
    navigator.clipboard.writeText(comment);
    alert('Copied to clipboard!');
  };

  return (
    <div className="app">
      <h1>PRGPT Dashboard</h1>
      {prs.map(pr => (
        <div key={pr.id} className="pr-card">
          <h2>PR #{pr.id}</h2>
          <p>Summary: {pr.summary}</p>
          <ul>
            {pr.reviewBullets.map((bullet, i) => <li key={i}>{bullet}</li>)}
          </ul>
          <button onClick={() => copyComment(pr.comment)}>Copy Comment</button>
        </div>
      ))}
    </div>
  );
}

export default App;