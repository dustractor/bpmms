from xml.dom import minidom

#{{{1 minidom setup
def _elem_inplace_addition(self,other):
    self.appendChild(other)
    return self
def _elem_textnode(self,text):
    textnode = self.ownerDocument.createTextNode(text)
    self.appendChild(textnode)
    return self
def _elem_set_attributes_from_tuple(self,*args):
    for k,v in args:
        self.setAttribute(k,str(v))
    return self
minidom.Element.__iadd__ = _elem_inplace_addition
minidom.Element.txt = _elem_textnode
minidom.Element.attrt = _elem_set_attributes_from_tuple
minidom.Element.__str__ = lambda s:s.toprettyxml().strip()

#}}}1
doc = minidom.Document()
elem = doc.createElement

root = elem("html")

head = elem("head")
root += head
title = elem("title")
head += title
title.txt("BPM / Milliseconds Delay Chart")
style = elem("style")
head += style
style.txt("""
table {
    border: #777 1px solid;
}

td {
    margin: 3rem;
    padding: 1rem;
}

tr {
    background-color:#ccc;
}
.bpm {
    font-weight:bold;
}

.dotted {
    background-color:#ccc0c0;
}
.triplet {
    background-color:#c0c0cc;
}
.headrow {
    color:#999;
}

""")

body = elem("body")
root += body

table = elem("table")
body += table

tr = elem("tr")
table += tr

td = elem("td")
tr += td
td.txt("BPM")

td = elem("td")
tr += td
td.txt("1/2")

td = elem("td")
tr += td
td.txt("1/4")

td = elem("td")
tr += td
td.txt("1/8")

td = elem("td")
tr += td
td.txt("1/16")

td = elem("td")
tr += td
td.txt("1/2T")
td.attrt(("class","triplet"))

td = elem("td")
tr += td
td.txt("1/4T")
td.attrt(("class","triplet"))

td = elem("td")
tr += td
td.txt("1/8T")
td.attrt(("class","triplet"))

td = elem("td")
tr += td
td.txt("1/2D")
td.attrt(("class","dotted"))

td = elem("td")
tr += td
td.txt("1/4D")
td.attrt(("class","dotted"))

td = elem("td")
tr += td
td.txt("1/8D")
td.attrt(("class","dotted"))


for n in range(40,260):
    if n%10==0:
        tr = elem("tr")
        table += tr
        tr.attrt(("class","headrow"))

        td = elem("td")
        tr += td
        td.txt("BPM")

        td = elem("td")
        tr += td
        td.txt("1/2")

        td = elem("td")
        tr += td
        td.txt("1/4")

        td = elem("td")
        tr += td
        td.txt("1/8")

        td = elem("td")
        tr += td
        td.txt("1/16")

        td = elem("td")
        tr += td
        td.txt("1/2T")
        td.attrt(("class","triplet"))

        td = elem("td")
        tr += td
        td.txt("1/4T")
        td.attrt(("class","triplet"))

        td = elem("td")
        tr += td
        td.txt("1/8T")
        td.attrt(("class","triplet"))

        td = elem("td")
        tr += td
        td.txt("1/2D")
        td.attrt(("class","dotted"))

        td = elem("td")
        tr += td
        td.txt("1/4D")
        td.attrt(("class","dotted"))

        td = elem("td")
        tr += td
        td.txt("1/8D")
        td.attrt(("class","dotted"))


    halfnote_ms = 120000 / n
    quarternote_ms = 60000 / n
    eighthnote_ms = 30000 / n
    sixteenthnote_ms = 15000 / n
    thirtysecondnote_ms = 7500 / n

    triplet_halfnote_ms = (halfnote_ms / 3) * 2
    triplet_quarternote_ms = (quarternote_ms / 3) * 2
    triplet_eighthnote_ms = (eighthnote_ms / 3) * 2

    dotted_halfnote_ms = halfnote_ms + quarternote_ms
    dotted_quarternote_ms = quarternote_ms + eighthnote_ms
    dotted_eightnote_ms = eighthnote_ms + sixteenthnote_ms 
    dotted_sixteenthnote_ms = sixteenthnote_ms + thirtysecondnote_ms

    tr = elem("tr")
    table += tr

    td = elem("td")
    tr += td
    td.txt(f"{n} bpm")
    td.attrt(("class","bpm"))

    td = elem("td")
    tr += td
    td.txt(f"{halfnote_ms:3.3f}")
    td = elem("td")
    tr += td
    td.txt(f"{quarternote_ms:3.3f}")
    td = elem("td")
    tr += td
    td.txt(f"{eighthnote_ms:3.3f}")
    td = elem("td")
    tr += td
    td.txt(f"{sixteenthnote_ms:3.3f}")

    td = elem("td")
    tr += td
    td.txt(f"{triplet_halfnote_ms:3.3f}")
    td.attrt(("class","triplet"))
    td = elem("td")
    tr += td
    td.txt(f"{triplet_quarternote_ms:3.3f}")
    td.attrt(("class","triplet"))
    td = elem("td")
    tr += td
    td.txt(f"{triplet_eighthnote_ms:3.3f}")
    td.attrt(("class","triplet"))

    td = elem("td")
    tr += td
    td.txt(f"{dotted_halfnote_ms:3.3f}")
    td.attrt(("class","dotted"))
    td = elem("td")
    tr += td
    td.txt(f"{dotted_quarternote_ms:3.3f}")
    td.attrt(("class","dotted"))
    td = elem("td")
    tr += td
    td.txt(f"{dotted_eightnote_ms:3.3f}")
    td.attrt(("class","dotted"))

# print(str(root))

with open("bpm_ms_chart.html","w",encoding="UTF8") as f:
    f.write(str(root))
