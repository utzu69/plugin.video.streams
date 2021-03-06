import xbmc, xbmcgui
import os, os.path, re
import glob
from glob import addon_log, ADDON_PATH, Downloader, message, addon

def grab_vk_stream(name, url):
  temp = os.path.join(ADDON_PATH,"temp.htm")
  Downloader(url, temp, addon.getLocalizedString(30065), name)  #Downloading page for parsing stream url
  f = open(temp)
  source_txt = f.read()
  f.close()
  os.remove(temp)
  
  #addon_log(source_txt)
  match=re.compile('url720=(http:\/\/[\w\W]+?.mp4)&').search(source_txt)
  if match:
    stream_url = match.group(1)
    addon_log('720 = '+stream_url)  
    return stream_url
  
  match=re.compile('url480=(http:\/\/[\w\W]+?.mp4)&').search(source_txt)
  if match:
    stream_url = match.group(1)
    addon_log('480 = '+stream_url)  
    return stream_url
  
  match=re.compile('url360=(http:\/\/[\w\W]+?.mp4)&').search(source_txt)
  if match:
    stream_url = match.group(1)
    addon_log('360 = '+stream_url)  
    return stream_url
    
  match=re.compile('url240=(http:\/\/[\w\W]+?.mp4)&').search(source_txt)
  if match:
    stream_url = match.group(1)
    addon_log('240 = '+stream_url)  
    return stream_url

  return None