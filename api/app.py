const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

app.post('/webhook', async (req, res) => {
  const { action, pull_request } = req.body;
  if (action === 'opened' || action === 'synchronize') {
    const prId = pull_request.id;
    // Trigger worker (simulated for now)
    console.log(`Received PR ${prId}, queuing for analysis`);
    res.status(200).send('Webhook received');
  } else {
    res.status(400).send('Unsupported action');
  }
});

app.listen(3000, () => console.log('API running on port 3000'));