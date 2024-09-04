const https = require("https");

https
    .get(`https://reqres.in/api/users`, resp => {
        let data = "";
        resp.on("data", chunk => {
            data += chunk
        });

        resp.on("end", () => {
            let url = JSON.parse(data).message;
            console.log(url);
        });
    })
    .on("error", err => {
        console.log("Error: " + err.message);
    })