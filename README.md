# Python Script for Finding Best Times to play Sports

A basic Python script, using tkinter, requests, and datetime to call an api to return weather data for your entered city and state. 

The script calculates the best date and time to play for the next 15 days, per hour. These are also graded by `Good`, `Great`, or `Best`. Good refers to when the tempurature in `F` is between `65 and 85`; and also less than `60% humidity`, and bewtween a `0 - 10 percent chance of precipitation`. Great is when the temp is `greater than 75` and also `in the humidity range`. Great is when the temp is `greater than 75` and the `humidity is less than 50%`.

## Screenshots

<p align="center">
  <img src="https://github.com/vs0t/Best-Days-For-Soccer/assets/125901041/55dc2102-f2c7-449f-ac31-a50bfe0ddc61" alt="placeholder">
</p>


## Installation

Clone repo with git clone

```bash
  git clone https://github.com/vs0t/Best-Soccer-Times-Finder.git
```

Move into the new download

```bash
  cd Best-Soccer-Times-Finder
```
Create .env file and add API_KEY
```bash
API_KEY=key
```

From here, you can either run the script, or double click.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file as mentioned above.

`API_KEY`=`own-key`
## Usage

```bash
python main.py
```

Enter City and State, and click "Get Results"

From here, it will peform the caluclation. If no good times are found, it lets the user know. If their is, it will display it initially, also displaying additional buttons to query search results


## Appendix

This is a very simple script, I mostly made this to to re-learn some forgotten Python components. This is in no way final product, just something I thought of and acted on as a quick little hour long side project.

## Authors

- [@vs0t](https://www.github.com/vs0t)


## License

[MIT](https://choosealicense.com/licenses/mit/)
