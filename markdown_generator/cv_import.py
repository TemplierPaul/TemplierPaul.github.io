import os
import yaml

def get_data(path):
    with open(path, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def make_paper(paper):
    paper["url_slug"]=paper["title"].replace(" ", "-").lower()
    paper["date"]=str(paper["date"])
    
    md_filename = str(paper["date"]) + "-" + paper["url_slug"] + ".md"
    html_filename = str(paper["date"]) + "-" + paper["url_slug"]
    year = paper["date"][:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + paper["title"] + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if "excerpt" in paper:
        md += "\nexcerpt: '" + html_escape(paper["excerpt"]) + "'"
    
    md += "\ndate: " + str(paper["date"]) 
    
    md += "\nvenue: '" + html_escape(paper["conference"]) + "'"
    
    md += "\nauthors: '" + html_escape(paper["authors"]) + "'"
    
    if "link" in paper:
        md += "\npaperurl: '" + paper["link"] + "'"
        
    if "code" in paper:
        md += "\ncodeurl: '" + paper["code"] + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    if "excerpt" in paper:
        md += "\n" + html_escape(paper["excerpt"]) + "\n"
    
    if "link" in paper:

        md += "\n[Download paper here](" + paper["link"] + ")\n" 
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
    return md_filename

def make_project(item):
    item["url_slug"]=item["title"].replace(" ", "-").lower()

    md_filename = str(item["date"]) + "-" + item["url_slug"] + ".md"
    html_filename = str(item["date"]) + "-" + item["url_slug"]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item["title"] + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /portfolio/""" + html_filename
    
    if "tagline" in item:
        md += "\nexcerpt: '" + html_escape(item["tagline"]) + "'"
    
    if "link" in item:
        md += "\npaperurl: '" + item["link"] + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    if "tagline" in item:
        md += "\n" + html_escape(item["tagline"]) + "\n"
    
    if "link" in item:
        md += "\n[Repository](" + item["link"] + ")\n" 
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_portfolio/" + md_filename, 'w') as f:
        f.write(md)
    return md_filename
