# WJX_Auto_Fill
Auto fill your personal info to wjx.cn using selenium.webdriver

# It supports..
1. Text box
2. radioCheck box
3. Select box

# Todo..
1. table text box
2. underline text box

# How to use
1. Download the `.py` file and `.json` file
2. Change the `config_example.json` to `config.json` after configuration
3. Fill the sheets of wjx.cn in 1 sec LOL

# Configuration Guide
`The content of a Question`: It means the major content of the question and determains what kind of info to input

`key_words`: If the one of the key_words appears in the title, we determine that the corresponding content(key) should be the return value of the function `define_question_kind`

`input`: 

Text box: This will be fully filled into the Text box

Check box: any option that contains it in the title will be checked

Selector: any option that contains it in the option will be selected

# Configuration Example
```
{
    "姓名": {
        "key_words": [
            "姓名",
            "名字"
        ],
        "input": "Sduby22"
    }
}
```
