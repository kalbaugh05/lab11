# Lab 11 - Presidio Anonymizer
No if/elif chains are used

Python dictionary

The AnonymizerEngine selects an operator dynamically at runtime. Each operator implements the same interface (`operate()`), allowing interchangeable strategies. Adding new operators (like `Initial`) requires minimal changes and doesn’t affect client code.