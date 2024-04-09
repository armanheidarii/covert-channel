const express = require('express')

const offset = 1000
const size = 128

const end_port = 4444

const port_activation = async (port) => {
    const app = express()

    app.get('/', (req, res) => {
        if (!req.body) {
            if (port == end_port)
                console.log()
            else
                process.stdout.write(String.fromCharCode(port - offset));
            return res.send('ok')
        }

        return res.status(404).send('You can not have body!')
    })

    app.listen(port, () => {
        console.log(`Example app listening on port ${port}`)
    })
}

for (let i = offset; i < offset + size; i++) {
    port_activation(i)
}

port_activation(end_port)
