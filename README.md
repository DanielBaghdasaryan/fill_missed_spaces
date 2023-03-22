# Fill missed spaces

Service to fill missed spaces in the text

### Requirements:
python3 environment (tested on python 3.8)
### Installation:
Run `pip install -r requirements.txt` inside project's directory
### Running:
Run

`python main.py`

<sub>* it might be `python3` for your environment</sub>

Server will run on http://127.0.0.1:5000/ 

> **Note**
>
>If you want to specify another port (e.g. 3000), just run
>
>`python main.py 3000`

> **Note**
>
>Please check the last line of the output. It should looks like
>
>`Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
> 
> To be sure server runs successfully

Then you could send POST request to URL: http://127.0.0.1:5000/ with following Body

```json
{
    "text": "Exampletext"
}
```

The response should looks like this:

```json
{
    "corrected_text": "Example text",
    "missed_space_positions": [
        7
    ]
}
```
