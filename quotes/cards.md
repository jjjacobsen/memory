# Quotes - Card Template

This note type has one card template that creates "Who said this?" flashcards for memorable quotes.

## Card Template

### Front
```
<p style="text-align: center;">Who said the following?</p>

<p style="font-style: italic; text-align: center;">"{{Quote}}"</p>
```

### Back
```
{{FrontSide}}

<hr id=answer>

{{Name}}
```

## How It Works

- **Question**: Displays the quote in italics and centered, asking who said it
- **Answer**: Shows the full question again, followed by the person's name
- The quote is automatically wrapped in quotation marks in the template
- All text is center-aligned for better visual presentation

## Example

**Front:**
```
Who said the following?

"Imagination is more important than knowledge"
```

**Back:**
```
Who said the following?

"Imagination is more important than knowledge"

――――――――――――――――――――――――――――――

Albert Einstein
``` 
