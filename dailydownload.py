from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.core.display import HTML
import re
import webbrowser


def path_to_image_html(path):
    if len(path)==0:
        return path
    else:
        return '<img src="'+ path + '" height="120" >'
    
def open_in_browser(fname):
    new = 2 # open in a new tab, if possible
    url = r"C:\Users\alexb\OneDrive\Documents\Python Scripts\{}".format(fname+'_.html')
    webbrowser.open(url,new=new)

def listitems(url,container,item1,item2,item3):
    founditems = []
    headers = { 'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, features="lxml")
    bundle = soup.findAll(container[0], attrs={"class" : container[1]})
    for i in bundle :
        item_title = i.find(item1[0], attrs={"class" : item1[1]})
        item_info = i.find(item2[0], attrs={"class" : item2[1]})
        images = i.findAll(item3[0])#.text
        #print(images)
        if len(images)==0:
            image=''
            #break
        else:
            for imageitem in images:
                try:
                    image = (imageitem['data-src'])
                    break
                except:
                    image = (imageitem['src'])
                    break
        try:
            title = str(item_title.text).strip() #[0].split("-").strip()
        except:
             #print(bundle)
             break
        #info = str(item_info.text).strip().split("£")
        founditems.append({"1":title, "2": item_info.text.replace('\n','<br>'),"3":image})
        output = pd.DataFrame(founditems)
        output.columns = ['Title','Details','Preview']
        # Rendering the images in the dataframe using the HTML method.
        HTML(output.to_html(escape=False,formatters=dict(Preview=path_to_image_html)))
        # Saving the dataframe as a webpage
        fname = re.sub('[\W_]+', '', url[0:20])
        output.to_html(fname+'_.html',escape=False, formatters=dict(Preview=path_to_image_html))
    open_in_browser(fname)
    return output


"""
psprices = listitems("https://psprices.com/region-gb/collection/lowest-prices?platform=PS4",
                    container=["div","content__game_card"],#content__game_card  component--game-card
                    item1=["span","title"],
                    item2=["span","content__game_card__discount"],
                    item3=["img","game-card--image entered loaded"])
"""



try:
    itad = listitems("https://isthereanydeal.com/?by=trending:desc",
                        container=["div","game"],
                        item1=["a","noticeable"],
                        item2=["div","deals dyn-semi"],
                        item3=["img","hoverZoomLink"])
except:
    print('fail')
    
try:
    amazon = listitems("https://www.amazon.co.uk/gp/video/search/ref=atv_hm_hom_c_gbpna7_8_smr?queryToken=eyJ0eXBlIjoicXVlcnkiLCJuYXYiOnRydWUsInBpIjoiZGVmYXVsdCIsInNlYyI6ImNlbnRlciIsInN0eXBlIjoic2VhcmNoIiwicXJ5Ijoibm9kZT0zMDEwMDg1MDMxLDIxMDk4NTg2MDMxLDMwNDY3MzcwMzEmZmllbGQtd2F5c190b193YXRjaD03NDQ4NjYyMDMxJnBfbl9lbnRpdHlfdHlwZT05NzM5OTUyMDMxJmFkdWx0LXByb2R1Y3Q9MCZicT0obm90IGF2X2tpZF9pbl90ZXJyaXRvcnk6J0dCJykmYmJuPTIxMDk4NTg2MDMxJnNvcnQ9LXByaW1lX3ZpZGVvX3N0YXJ0X2RhdGUmcndfaHRtbF90b193c3JwPTEmaT1pbnN0YW50LXZpZGVvJnBfbl93YXlzX3RvX3dhdGNoPTc0NDg2NjIwMzEmc2VhcmNoLWFsaWFzPWluc3RhbnQtdmlkZW8mcXMtYXZfcmVxdWVzdF90eXBlPTQmcXMtaXMtcHJpbWUtY3VzdG9tZXI9MiIsInJ0IjoiZ2JQTmE3c21yIiwidHh0IjoiTmV3IG1vdmllcyBldmVyeSBkYXkiLCJvZmZzZXQiOjAsIm5wc2kiOjAsIm9yZXEiOiIxN2ViNWJlZC01ZDhiLTQ5MzctOTdjZC05MjM3YzkwZjk3MTY6MTYyNTQxNzk5MTAwMCIsInN0cmlkIjoiMToxVlcxQTNCR0NWTkRZIyNNWlFXR1pMVU1WU0VHWUxTTjUyWEdaTE0iLCJvcmVxayI6Im1qeEROOFpIZGFUZVZaNWtMZW5IcmNaYXVwakhXYm9kNHFXcFZwemFRaUE9Iiwib3JlcWt2IjoxfQ%3D%3D&pageId=default&queryPageType=browse&ie=UTF8",
                          container=["div","_1y15Fl dvui-beardContainer D0Lu_p av-grid-beard"],#["div","_1N2P-J mustache _2mxudr"],
                          item1=["div","vRplU5"],
                          item2=["div","padded-beard-info-container"],
                          item3=["img","hoverZoomLink"])
except:
    print('fail')
    
try:
    psndeals = listitems("https://psndeals.com/ps4-store-gb-hot-deals/",
                          container=["div","game-card"],
                          item1=["h3","game-card-title"],
                          item2=["p","game-card-text"],
                          item3=["img","lazy loaded"])
except:
    print('fail')
    
try: 
    steamggdeals = listitems("https://gg.deals/deals/?store=4",
                        container=["div","cta-ext"],
                        item1=["div","title-line"],
                        item2=["div","deal-hoverable price-wrap"],
                        item3=["img","hoverZoomLink"])
except:
    print('fail')
    
try:
    gogggdeals = listitems("https://gg.deals/deals/?store=10",
                        container=["div","cta-ext"],
                        item1=["div","title-line"],
                        item2=["div","deal-hoverable price-wrap"],
                        item3=["img","hoverZoomLink"])
except:
    print('fail')


