#Filename: HTML_generator.py
#Date Created: 05-07-2015
#Revision: 1.0
#Assciated File: n/a
#Purpose: Demonstrates use of while loops and functions to create HTML
#Input(s): text string
#Output(s): HTML
#Passed Python error check: 05-07-2015
#******************************Programming Code Starts Here****************************
#
#
sample_text = """TITLE: Computational Problem Solving
DESCRIPTION: Abstract thinking is the lion's share of solving any computation problem
because you must first understand the problem.
TITLE: Understanding of Functions
DESCRIPTION: Functions are critical to eliminating repetition and reducing human error.
TITLE: An Introduction to Lists
DESCRIPTION: There are two major differences between lists and strings.  First, strings 
contain only characters whereas lists can contain anything.  
Second, lists can support something called Mutation"""

#This function combines title and description to create HTML
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

#This code locates and returns the concept title
def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

#This code locates and returns the concept description
def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

#This code locates a concept by using the concept number
def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

#This code generates the final HTML output.
def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(sample_text)