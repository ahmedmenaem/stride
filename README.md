



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Strade</h3>

  <p align="center">
    Products and brands api
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Run Scripts</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project is called Stride is a rest api for products craweled from top websites selling shoes

### Built With

This app is built using
* [Python]()
* [pymongo]()
* [mongodb]()
* [beatifulSouap]()
* [pipenv]()
* [docker]()



### Prerequisites

Install pipenv
* npm
  ```sh
  sudo pip install pipenv
  ```

### Installation

1. Make sure you have a pipenv and you run mongo db instance
```sh
    docker run --name mongo -p 27017:27017 -d mongo
```
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Run pipenv shell
   ```sh
   pipenv shell
   ```
4. Install deps
   ```sh
   pipenv install
   ```
5. Run app
    ```sh
    python app.py
    ```


### Run script to clean the crawled data and save it to mongo db
1. index sites
    ```sh
      python ./scripts/index_sites.py  
    ```
1. index brands
    ```sh
      python ./scripts/index_brands.py  
    ```
1. index products
    ```sh
      python ./scripts/index_products.py  
    ```


<!-- USAGE EXAMPLES -->
## Usage

You can use Postman or httpie to access the Rest endpoing
1. Get the index sites
```sh
    http :5000/sites page==1
```
2. Get brands
```sh
    http :5000/brands
```
3. Get products
```sh
    http :5000/products page==1 brand==Zara
```
4. Get product details
```sh
    http :5000/products/:id
```
