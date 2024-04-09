require('dotenv').config({ path: '../.env' })

const express = require('express')

const offset = 1000
const size = 128

const end_port = 4444

console.log("Please Enter Your Time Interval First In .env file")
const interval = process.env.INTERVAL + process.env.THRESHOLD
last_req_time = 0

const port_activation = async (port) => {
    const app = express()

    app.get('/', (req, res) => {
        now = Date.now()
        time = 0
        if (last_req_time)
            time = (now - last_req_time) / 1000
        last_req_time = now
        if (!req.body && time < interval) {
            if (port == end_port)
                console.log()
            else
                process.stdout.write(String.fromCharCode(port - offset));
            return res.send('ok')
        }

        return res.status(400).send('You can not have body!')
    })

    app.listen(port, () => {
        console.log(`Example app listening on port ${port}`)
    })
}

for (let i = offset; i < offset + size; i++) {
    port_activation(i)
}

port_activation(end_port)
