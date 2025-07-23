# U.S. Presidents - Detail - Card Template

This note type has one card template that creates question-answer flashcards about presidential facts.

## Card Template

### Front
```
Which president {{Detail}}
```

### Back
```
{{FrontSide}}

<hr id="answer">

{{Name}}
<br>
{{#Extra}}
<br><em>{{Extra}}</em>
{{/Extra}}
```

## How It Works

- **Question**: Uses the Detail field to create a "Which president..." question
- **Answer**: Shows the president's name, with optional extra information in italics
- The `{{#Extra}}` conditional formatting ensures the Extra field only displays when it contains content
- The `<hr id="answer">` creates a visual separator between question and answer

## Example

**Front:**
```
Which president completed the Louisiana Purchase
```

**Back:**
```
Which president completed the Louisiana Purchase

――――――――――――――――――――――――――――――

Thomas Jefferson

(1803) Doubled U.S. territory
``` 
