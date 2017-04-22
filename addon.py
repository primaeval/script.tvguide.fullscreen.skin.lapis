import xbmc,xbmcgui,xbmcaddon

SKINS = [["Lapis", "Lapis"],
         ["Lapis with Categories",  "LapisC"]]


d = xbmcgui.Dialog()
names = [s[0] for s in SKINS]
skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
if skin > -1:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.lapis/')
        tvgf.setSetting('skin.user', SKINS[skin][1])
        tvgf.setSetting('categories.background.color', '[COLOR ff696969]midnightblue[/COLOR]')
        tvgf.setSetting('epg.nofocus.color', '[COLOR ffd3d3d3]aliceblue[/COLOR]')
        tvgf.setSetting('epg.focus.color', '[COLOR ffffffff]blue[/COLOR]')
        tvgf.setSetting('timebar.color', '[COLOR ffb22222]yellow[/COLOR]')
        tvgf.setSetting('epg.video.pip', 'true')
        tvgf.setSetting('program.image.scale', 'true')
        tvgf.setSetting('program.background.image.source', '0')
        tvgf.setSetting('program.background.color', '[COLOR ff606060]midnightblue[/COLOR]')
        tvgf.setSetting('program.background.flat', 'true')
        tvgf.setSetting('action.bar', 'false')