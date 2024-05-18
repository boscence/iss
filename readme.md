# Where is the ISS? 🚀

[![ISS Image]](https://media.wired.com/photos/5d0015546874e00ab2efb677/master/pass/science_iss_iss056e201352.jpg)

A simple Flask web application that shows you the real-time location of the International Space Station (ISS). 

## Why? 🤔
This is a personal project to improve my experiences in flask and git/github.
It's a simple project that I use to improve my personal coding practices through experience.

## Tech 🤖
- **Python:** Nothing special here.
- **Flask:** A very simple implementation.
- **Git:** I have used github Codespaces, this is new to me.

## Features ✨
- **Live Tracking:** See the ISS's current position.
- **Nearest Country:** 🚧 In Progress 🚧 See which country the ISS is over, or the nearest country if it's not over land. 

## How it Works 🛰️
2. **Fetches Data:** Requests the latest ISS location data from the API.
3. **Processes Data:** It parses the JSON response to extract relevant information.
4. **GeoLocates:** 🚧 In Progress 🚧 It determines the country the ISS is over, or the nearest country if it's not over land.

## Installation 🛠️

1. **Clone Repository:**
   ```bash
   git clone https://github.com/boscence/iss
   python -m flask run