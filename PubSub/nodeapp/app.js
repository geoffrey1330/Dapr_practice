// ------------------------------------------------------------
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.
// ------------------------------------------------------------

const express = require('express');
const bodyParser = require('body-parser');

const app = express();
// Dapr publishes messages with the application/cloudevents+json content-type
app.use(bodyParser.json({ type: 'application/*+json' }));

const port = 3000;

app.get('/dapr/subscribe', (_req, res) => {
    res.json([
        {
            pubsubname: "pubsub",
            topic: "order",
            route: "order"
        },
        {
            pubsubname: "pubsub",
            topic: "email",
            route: "email"
        }
    ]);
});

app.post('/order', (req, res) => {
    console.log("order: ", req.body.data.message);
    res.sendStatus(200);
});

app.post('/email', (req, res) => {
    console.log("email: ", req.body.data.message);
    res.sendStatus(200);
});

app.listen(port, () => console.log(`Node App listening on port ${port}!`));
