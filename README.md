[![Docker Build Status](https://img.shields.io/docker/build/jrottenberg/ffmpeg.svg)](https://github.com/e8kor/deton)

## API

|Method | Url           | Payload                                        | Description                         |
|:------|:--------------|:-----------------------------------------------|:------------------------------------|
|GET    | /health       |                                                | Check service availability          |
|GET    | /roulette     |                                                | Redirect to url from roulette pool  |
|GET    | /{short-name} |                                                | Redirect to named url               |
|POST   | /{short-name} | `{"url": "http://goo.gl"}`                     | Create a shortlink                  |
|POST   | /{short-name} | `{"url": "http://goo.gl", "roulette": true  }` | Create a shortlink with roulette    |
|POST   | /{short-name} | `{"url": "http://goo.gl", "roulette": false }` | Create a shortlink with no roulette |
|PUT    | /{short-name} | `{"url": "http://goo.gl"}`                     | Override shortlink named after {short-name} with no roulette|
|PUT    | /{short-name} | `{"url": "http://goo.gl", "roulette": true  }` | Override shortlink named after {short-name} with roulette   |
|PUT    | /{short-name} | `{"url": "http://goo.gl", "roulette": false }` | Override shortlink named after {short-name} with no roulette|