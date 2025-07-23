# U.S. Presidents - Info - Card Templates

This note type has seven card templates that test different aspects of presidential information.

## Card Templates

### 1. Name to Number

**Front:**
```
What number president was {{Name}}
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Number}}
```

### 2. Number to Name

**Front:**
```
Who was president {{Number}}?
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Name}}
```

### 3. Name to Term

**Front:**
```
What were the years {{Name}} was in office?
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Term}}
```

### 4. Term to Name

**Front:**
```
Who was president from {{Term}}?
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Name}}
```

### 5. Name to Party

**Front:**
```
What political party did {{Name}} belong to?
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Party}}
```

### 6. Portrait to Name

**Front:**
```
<p>Who is this?</p>

<div style="text-align: center;">
  {{Portrait}}
</div>
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{Name}}
```

### 7. Name to State

**Front:**
```
What state did {{Name}} represent?
```

**Back:**
```
{{FrontSide}}

<hr id=answer>

{{State}}
```

## How It Works

- Each card template tests a different piece of presidential information
- All cards follow the same basic format: question on front, answer after separator on back
- The portrait card includes HTML styling to center the image
- Cards can be selectively enabled/disabled in Anki based on study preferences

## Examples

**Name to Number:**
- Front: "What number president was Abraham Lincoln"
- Back: "16"

**Portrait to Name:**
- Front: Shows centered portrait image with "Who is this?"
- Back: "George Washington"

**Term to Name:**
- Front: "Who was president from 1933-1945?"
- Back: "Franklin D. Roosevelt" 
