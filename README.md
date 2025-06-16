# ZeroDay-httpbomb
The script sends a high volume of randomized HTTP GET, POST, PUT, and DELETE requests to a target URL

# HTTPFlood - Educational Layer 7 HTTP Flood DoS Tool

> **DISCLAIMER:**  
> This tool is **strictly for educational and authorized penetration testing in controlled environments**.  
> Do not use against any server without explicit permission. Misuse may be illegal and unethical.

---

## Overview

**HTTPFlood** is a Python-based script designed for cybersecurity trainers, students, and lab demonstrators to showcase the effects and mechanics of Layer 7 (application layer) HTTP flood attacks.  
It generates high volumes of randomized HTTP requests (GET, POST, PUT, DELETE) to overwhelm test web servers, demonstrating the importance of web application security and mitigation techniques.

---

## Features

- Multi-threaded, high-throughput HTTP request generation
- Randomized HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- Randomized user agent strings and request payloads
- Colorized, real-time status output for easy monitoring (green for sent, red for errors)
- Easy-to-use command-line interface

---

## Usage

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/httpflood.git
cd httpflood
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Run the Script

```sh
python httpflood.py -u http://127.0.0.1:8080
```

- Replace `http://127.0.0.1:8080` with the address of your test server.
- **Do not use this tool on external or unauthorized systems.**

---

## Example Output

```
[GET] Sent: 200
[POST] Sent: 200
[DELETE] Error: ...
...
```
*Status messages appear in green for successful requests, red for errors.*

---

## Customization

You can adjust the following parameters in `httpflood.py` for your lab/demo needs:

- `THREADS`: Number of concurrent threads (default: 50)
- `REQUESTS_PER_THREAD`: Number of requests per thread (default: 250)

---

## Ethical & Legal Notice

- **Use only in environments you own or have explicit permission to test.**
- This project is for learning and simulation only.  
- Unauthorized use is strictly prohibited and may violate laws and ethics.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

Praveen-7777

---

## Contributing

Contributions, improvements, and educational resources are welcome!  
Open an issue or pull request on GitHub.

