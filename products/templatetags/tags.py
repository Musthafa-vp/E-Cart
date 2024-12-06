from django import template

register=template.Library()

@register.filter(name='tags')
def tags(list,tag_size):
    tags=[]
    i=0
    for data in list:
        tags.append(data)
        i+=1
        if i==tag_size:
            yield tags
            i=0
            tags = []
    if tags:
        yield tags        
