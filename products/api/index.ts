import express, { Application } from 'express';
import dotenv from 'dotenv';

const app: Application = express();

const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.send('HELLO WORLD');
});

app.listen(port, () => {
  console.log('server is running on ', port);
});
