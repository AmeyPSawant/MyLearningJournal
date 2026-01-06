# Apex Basics for Admins\

## Get Started with Apex

The Developer Console is a tool that developers use to create and edit files of code.

Follow these steps to access the Developer Console.

1. First, make sure you are logged in to Trailhead.
2. Then, click your user avatar in the upper-right corner of this page and select Hands-on Orgs from the dropdown.
3. Click the username to launch your org. Want to create a new org? See the Trailhead Playground Management module to learn how.
4. In your Trailhead Playground, click Setup and select Developer Console.

```
To Create a New Apex Class, click on File > New > Apex Class
Single line comments using // Comment
Multiline comments using /* Comment */
```

## Practice in the Developer Console

In this module I learned how to utilize _Open Execute Anonymus Window_ to test and debug code.  
Also to utilize the Execution Log.

## Use Collections

In this module I learned how to declare and initialize a list and two ways to add items to a list.

```
String[] groceries = new String[4];
System.debug('Groceries: ' + groceries);
groceries.add('Tea');
groceries.add('Sugar');
System.debug('Added 2 items: ' + groceries);
groceries.add(1, 'Honey');
System.debug('Added Honey in index 1: ' + groceries);
System.debug('Item 0: ' + groceries[0]);
```

Output:  
<img src="Use_Collections_Output.png" alt="Use Collections Output" width="500px">

## Control Data Flow

### Comparison Operators

| Operator | Description              | Syntax Examples        | Result |
| -------- | ------------------------ | ---------------------- | ------ |
| `<`      | Less than                | `1 < 2`                | TRUE   |
| `<=`     | Less than or equal to    | `1 <= 2`, `3 <= 3`     | TRUE   |
| `==`     | Equal to                 | `10 == 10`             | TRUE   |
| `!=`     | Not equal to             | `10 != 0`              | TRUE   |
| `<>`     | Not equal to (alternate) | `10 <> 11`             | TRUE   |
| `>`      | Greater than             | `11 > 10`              | TRUE   |
| `>=`     | Greater than or equal to | `40 >= 10`, `40 >= 40` | TRUE   |

### Conditional Statements

#### If-Else Statements

```
if(condition is true) {
    //do this
} else {
    //do this
}
```

#### If-Else If Statements

```
if(condition is true) {
    //do this
} else if {
    //do this
} else {
    //do this
}
```

#### Switch Statements

```
switch on expression {
    when value1 {
        //code block 1
    }
    when value2 {
        //code block 2
    }
    when else { //if none of the previous values apply
        //code block 3
    }
}
```

### Logical Operators

#### AND

Operator Symbol - &&  
Psuedocode - If X _and_ Y, do this. Otherwise, do that.  
Apex Code -

```
if(X && Y) {
//do this
} else {
//do this
}
```

#### OR

Operator Symbol - ||
Psuedocode - If X _or_ Y, do this. Otherwise, do that.  
Apex Code -

```
if(X || Y) {
//do this
} else {
//do this
}
```

## Use Loops

### While

```
While(condition) {
    //run this block of code
}
```

### Do While

```
Do {
    //run this block of code
} while(condition);
```
