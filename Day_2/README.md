# Week 9 Class 2 – Python Collections

## Project Overview

This project is part of the Charlotte Projects Week 9 Python training. It focuses on using Python collections to organise and analyse drilling sensor observations from different wells.

## Practical Activities

In this practical, I worked with eight sensor observations from six different wells using Python collections.

The activities covered:

- Lists of dictionaries for storing sensor observations.
- List indexing and slicing.
- Tuples for storing measurement units.
- Dictionaries for accessing and organising data.
- Sets for identifying unique well IDs and fields.
- Built-in functions such as `len()` and `sum()` for calculating summaries.
- Counting observations for each well.

## Reflection

Using a list of dictionaries is useful when working with drilling sensor observations because each observation can contain different information, such as well ID, pressure, temperature, sensor status and field. A list keeps the observations in their original order and allows repeated well IDs to remain in the data. This is important because one well can have more than one sensor reading at different times. Each dictionary makes it easy to access a particular value using its key. Sets can also help identify unique well IDs without removing the original observations. Overall, these collections make the data easier to organise, access and summarise using basic Python.

## How to Run

Make sure Python is installed, then run:

```bash
python student_collections_lab.py
```

## Files

- `student_collections_lab.py` – Completed Python practical.
- `datastructures01.py` – Class activity and personal practice.
- `submission_evidence/` – Screenshots of the practical output.