with open('/home/yejial/Desktop/data/WHL/whl-2010-2011/output-drafted-2010-2011.csv','r') as input:
    with open('/home/yejial/Desktop/data/WHL/whl-2010-2011/drated-position.csv','w') as output:
        writer=csv.writer(output,lineterminator='\n')
        reader=csv.reader(input)
        
        all=[]
        row=next(reader)
        row.append('position')
        row.append('player')
        all.append(row)
        for row in reader:
            #m=re.match('\((.+)/',row[1])
            #print row[1]
            m=re.search(r'\((.*?)\)',row[1]).group(1)
            pos=row[1].index("(")
            name=row[1][0:pos]
            print name
            if m.find("/")==-1:
                
                row.append(m)
                row.append(name)
                #print row
                all.append(row)
            else:
                x=re.search(r'(.+?)/',m).group(1)
                #print x
                row.append(x)
                row.append(name)
                #print row
                all.append(row)
            
        
        writer.writerows(all)
