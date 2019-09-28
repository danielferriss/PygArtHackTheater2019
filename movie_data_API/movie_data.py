import pandas as pd
import numpy as np
import sys
import requests
from lxml import html
from bs4 import BeautifulSoup
import urllib.parse

desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width,threshold=sys.maxsize)
pd.set_option('display.max_columns', 35)

global arrID
arrID = [""]

global arrBox
arrBox = [""]

def get_box_office(url):
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.find_all('b')[2])
    arrBox.append(soup.find_all('b')[2])

def return_movie_id_BoxOfficeMojo(url):
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, "lxml")
    str1 = "/movies/?id"
    for link in soup.find_all('a'):
        str2 = link.get('href')
        if str1 in str2:
            arrID.append(link.get('href'))

get_box_office("https://www.boxofficemojo.com/movies/?id=blaze2018.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=afaithfulman.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=afantasticwoman.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=aghoststory.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=harddaysnight14.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=leagueoftheirown.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=amancalledove.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=aquietpassion.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=aquietplace.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=aunitedkingdom.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=afterauschwitz.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=akira2021.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=alienlovetriangle.htm")











































get_box_office("https://www.boxofficemojo.com/movies/?id=aliveandkicking.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=allistrue.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=allthatheavenallows.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=allthequeenshorses.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=amazinggrace2019.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=americanwoman.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=andreirublev2018.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=annaandtheapocalypse.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=annihilation.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=apollo11.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=alienarrival.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=askdrruth.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ateternitysgate.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=audition.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=lego2.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=beatrizatdinner.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=beforewevanish.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=belledejour2018.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=birdsofpassage.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=bisbee17.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=blackgirl.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=blackkklansman.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=bladerunner-thefinalcut.htm")






























get_box_office("https://www.boxofficemojo.com/movies/?id=bladerunner-thefinalcut.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=bladerunnersequel.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=blaze2018.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=blindspotting.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=unirratedcomedy.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=bluecollarcomedytour.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=bombshell.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=valleyofbones.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=booksmart.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=border18.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=boyznthehood.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=italianjob2.htm")







get_box_office("https://www.boxofficemojo.com/movies/?id=burning.htm")
















get_box_office("https://www.boxofficemojo.com/movies/?id=butchcassidyandthesundancekid.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=cafesociety.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=canyoueverforgiveme.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=candyman2020.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=capefear.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=capernaum.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=casablanca.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=certainwomen.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=chavela.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=childrenofmen.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=christine201).htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=climax.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=closeencountersofthethirdkind.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=coldwar2018.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=colossalyouth.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=columbus.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=crooklyn.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=damsel.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=darkesthour2017.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=daughtersofthedust.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=dawnofthedead.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=dawsoncity:frozentime.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=demonic.htm")


























get_box_office("https://www.boxofficemojo.com/movies/?id=architectsofdenial.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=destroyer.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=dirtydancing13.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=disobedience.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=dolores.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=donniedarko.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=dontthinktwice.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=strangecaseofdrjekyllandmrhyde.htm")







get_box_office("https://www.boxofficemojo.com/movies/?id=echointhecanyon.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=elmarlamar.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=elle.htm")









get_box_office("https://www.boxofficemojo.com/movies/?id=endlesspoetry.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=ernestscaredstupid.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=meteugeneonegin.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=exlibris.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=exmachina.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=facesplaces.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=fannyandalexander.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=filmstarsdontdieinliverpool.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=filmworker.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=firstman.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=firstreformed.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=flashdance.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=frantzfanon.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=freesolo.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ganja2018.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=gattaca.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=blumhouse2.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=ghoststories.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=giantlittleones.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=gimmedanger.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=girlhood2015.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=gracejonesbnb.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=grease2.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=gremlins2.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=groundhogday.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=hagazussa.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=hailsatan.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=untitledblum2019c.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=hardtobeagod.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=lastchanceharvey.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=haveaniceday.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=henryportraitserialkiller.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=a24horrora.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=highlife.htm")







get_box_office("https://www.boxofficemojo.com/movies/?id=hotsummernights.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=hotelbytheriver.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=howtotalktogirlsatparties.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=huntforwilderpeople.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=iamcuba.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=iamnotawitch.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=iamnotyournegro.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=ifbealestreetcouldtalk.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=inthefade.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=indianajonesandthelastcrusade.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=indignation.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=isleofdogs.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ixcanul.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=jackie.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=jaws4.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=jimihendrixelectricchurch.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=jurassicpark3.htm")







get_box_office("https://www.boxofficemojo.com/movies/?id=kedi.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=keepquiet.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=kiki30.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=killerofsheep.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=bunuelinthelabyrinthoftheturtles.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=ladybird.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ladymacbeth.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=landline.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=latenight.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=leanonpete.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=lemon.htm")












get_box_office("https://www.boxofficemojo.com/movies/?id=letthecorpsestan.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=untitledlionsgatehorrorfilm.htm")







































get_box_office("https://www.boxofficemojo.com/movies/?id=littlemen2016.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=littlewoods.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=liyana.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=loandbehold.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=lobstercop.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=loganlucky.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=longdayjourneynight2019.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=lovingpablo.htm")
















get_box_office("https://www.boxofficemojo.com/movies/?id=lovingvincent.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=luce.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=furyroad.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=madelinesmadeline.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=maiden.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=manchesterbythesea.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=mandy.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=mariabycallas.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=marjorieprime.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=marlinathemurdererinfouracts.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=maryandthewitchsflower.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=marymagdalene.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=maryqueenofscots.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=maximumoverdrive.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=meetinggorbachev.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=menashe.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=miamadre.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ariastorhorror.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=mindingthegap.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=mirai.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=mississippimasala.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=montereypop.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=montypythonandtheholygrail.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=moonlightsonatadeafnessinthreemovements.htm")






















get_box_office("https://www.boxofficemojo.com/movies/?id=morrisfromamerica.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=mortalkombat2021.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=mrgaga.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=multiplemaniacs2016.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=mycousinrachel.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=myneighbortotoro.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=nancydrew2019.htm")





















get_box_office("https://www.boxofficemojo.com/movies/?id=nightlivingdead50.htm")









get_box_office("https://www.boxofficemojo.com/movies/?id=nomansland.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=nonfiction.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=norman2017.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=novitiate.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=obit.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=oceanwaves.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ohlucy.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=okkosinn.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=onthebeachatnightalone.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=oneweekandaday.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=ophelia.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=paddington2.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=pasolini.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=paterson.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=pavarotti.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=personalshopper.htm")
















get_box_office("https://www.boxofficemojo.com/movies/?id=petsematary2019.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=batmanmaskofthephantasm.htm")







get_box_office("https://www.boxofficemojo.com/movies/?id=paulthomasanderson2017.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=policestorydoublefeature.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=polyester.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=possession08.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=promnight07.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=punchdrunklove.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=rafiki.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=rbg.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=redjoan.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=revenge2018.htm")





































get_box_office("https://www.boxofficemojo.com/movies/?id=robotandfrank.htm")












get_box_office("https://www.boxofficemojo.com/movies/?id=rollerball.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=horriblehistories.htm")






















































get_box_office("https://www.boxofficemojo.com/movies/?id=rosemarysbaby.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=rubberneck.htm")









get_box_office("https://www.boxofficemojo.com/movies/?id=savingbrinton.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=scarletdiva.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=sciencefair.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=selma.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=meandmyshadow.htm")








































































get_box_office("https://www.boxofficemojo.com/movies/?id=shoplifters.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thesilence18.htm")






































get_box_office("https://www.boxofficemojo.com/movies/?id=skatekitchen.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=solaris2017.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=sorrytobotheryou.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=spacejam2.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=stalker2017.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=stanollie.htm")






























































get_box_office("https://www.boxofficemojo.com/movies/?id=stefanzweig.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=stepsisters.htm")






















































get_box_office("https://www.boxofficemojo.com/movies/?id=stopmakingsense.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=studio54.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=summer1993.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=superman2015.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=swordoftrust.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=trainspotting2.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=talesfromthehood.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=tangerine.htm")





get_box_office("https://www.boxofficemojo.com/movies/?id=ataxidriver.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=theaftermath.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=thebadbatch.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=beatleseightdaysaweek.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thebeguiled2017.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=bfg.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=biglebowski.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thebigsick.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=biggestlittlefarm.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=catechismcataclysm.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=bookoflife14.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=thecakemaker.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=withoutremorse.htm")









get_box_office("https://www.boxofficemojo.com/movies/?id=theclovehitchkiller.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=viperclub.htm")





























































get_box_office("https://www.boxofficemojo.com/movies/?id=thedeaddontdie.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thedeathofstalin.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=theendless.htm")
















get_box_office("https://www.boxofficemojo.com/movies/?id=blueexorcist.htm")












get_box_office("https://www.boxofficemojo.com/movies/?id=lynrydskynyrdlastofthestreetsurvivors.htm")

























get_box_office("https://www.boxofficemojo.com/movies/?id=thefavourite.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thefloridaproject.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=johnfogerty50yeartrip.htm")














get_box_office("https://www.boxofficemojo.com/movies/?id=grandbudapesthotel.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=theguilty.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=thehandmaiden.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=taleoftales.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=theheiresses.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=modestheroesponocshortfilmsvol1.htm")

























































































get_box_office("https://www.boxofficemojo.com/movies/?id=howling.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=theinnocents.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=theinsult.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=killingofasacreddeer.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=lastblackmaninsanfrancisco.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thelittlehours.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thelostcityofz.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thelovers.htm")






















get_box_office("https://www.boxofficemojo.com/movies/?id=thelure.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=themanwhokilleddonquixote.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=matrixrevolutions.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=themiseducationofcameronpost.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=muppetchristmascarol.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=nightofthehunter.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thenightingale.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=nuttyprofessor2.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=oldmanthegun.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=theornithologist.htm")









get_box_office("https://www.boxofficemojo.com/movies/?id=partysjustbeginning.htm")









































































get_box_office("https://www.boxofficemojo.com/movies/?id=joanofarc2017re.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=peoplevsfritzbauer.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=rockyhorrorpictureshow.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=escaperoom2.htm")

































































get_box_office("https://www.boxofficemojo.com/movies/?id=thesalesman.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=sandlot.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thesecondmother.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=theshapeofwater.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=texaschainsawmassacre2.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=treasureofthesierramadre70th.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thetriptospain.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=umbrellasofcherbourg04.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=usautism.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=thevoid.htm")








get_box_office("https://www.boxofficemojo.com/movies/?id=wailing.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thethirdwife.htm")












































get_box_office("https://www.boxofficemojo.com/movies/?id=thewound.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=zookeeperswife.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=thelma.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=theyshallnotgrowold.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=thoroughbreds.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=threeidenticalstrangers.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=tickled.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=titoandthebirds.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=tobeornottobe.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=tomoffinland.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=theroom.htm")










get_box_office("https://www.boxofficemojo.com/movies/?id=tonierdmann.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=tonimorrisonpiecesiam.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=toolatetodieyoung.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=transit.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=truthordare2017.htm")




get_box_office("https://www.boxofficemojo.com/movies/?id=twinpeaksfirewalkwithme.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=latwister.htm")






get_box_office("https://www.boxofficemojo.com/movies/?id=velvetgoldmine.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=viceroyshouse.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=weiner.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=wendyandlucy.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=whosestreets?.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=wildchild.htm")


















































































get_box_office("https://www.boxofficemojo.com/movies/?id=wildnightswithemily.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=wildlife18.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=willywonkaandthechocolatefactory.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=womanatwar.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=bemyneighbor.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=yellowsubmarine2018.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=youwereneverreallyhere.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=yourname.htm")


get_box_office("https://www.boxofficemojo.com/movies/?id=zama.htm")



get_box_office("https://www.boxofficemojo.com/movies/?id=alienarrival.htm")





#######################



'''
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blaze")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Bread Factory, Part One")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Faithful Man")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Fantastic Woman")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Ghost Story")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Hard Day's Night")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A League of Their Own")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Man Called Ove")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Matter of Life and Death")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Quiet Passion")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A Quiet Place")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=A United Kingdom")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=After Auschwitz")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Akira")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ali: Fear Eats the Soul")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Alien")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Alive and Kicking")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=All Is True")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=All That Heaven Allows")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=All the Queen's Horses")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Amazing Grace")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=American Woman")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ancien and the Magic Tablet")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Andrei Rublev")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Anna and the Apocalypse")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Annihilation")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Apollo 11")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Arrival")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ask Dr. Ruth")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=At Eternity's Gate")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Audition")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Batman: The Movie")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Beatriz at Dinner")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Before We Vanish")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Belladonna of Sadness")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Belle de Jour")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Beyond the Valley of the Dolls")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Bicycle Thieves")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Birds of Passage")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Bisbee '17")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Black Clover")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Black Girl")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=BlacKkKlansman")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blade")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blade Runner")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blade Runner 2049")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blaze")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blindspotting")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blockers")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Blue Collar")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Bombshell: The Hedy Lamarr Story")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Bones")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Booksmart")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Border")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Boyz n the Hood")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Brain Damage")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Brazil")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Burning")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Butch Cassidy and the Sundance Kid")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Buy Me a Gun")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Cafe Society")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Can You Ever Forgive Me?")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Candyman")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Cape Fear")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Capernaum")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Carmen Jones")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Casablanca")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Cemetery Without Crosses")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Certain Women")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Chavela")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Children of Men")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Christine")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Climax")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Close Encounters of the Third Kind")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Cold War")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Colossal")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Columbus")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Cooley High")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Crooklyn")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Damsel")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Darkest Hour")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Daughters of the Dust")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dawn of the Dead")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dawson City: Frozen Time")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Deconstructing the Beatles' White Album")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Deep Red")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Demon")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Denial")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Destroyer")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dilili in Paris")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dirty Dancing")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Disobedience")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dolores")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Donnie Darko")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Don't Think Twice")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dr. Jekyll and Mr. Hyde")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Dreaming of a Jewish Christmas")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Echo in the Canyon")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=El mar la mar")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Elle")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Empire of the Ants")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Endless Poetry")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Eraserhead")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ernest Scared Stupid")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Eugene Onegin")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ex Libris: The New York Public Library")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ex Machina")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Faces Places")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Fanny and Alexander")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Film Stars Don't Die in Liverpool")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Filmworker")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=First Man")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=First Reformed")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Flashdance")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Flower and Sword")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Foreign Body")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Frantz")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Free Solo")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ganja & Hess")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Gattaca")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Get Out")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ghost Stories")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Giant Little Ones")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Gimme Danger")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Girlhood")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Grace Jones: Bloodlight and Bami")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Grease")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Gremlins")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Groundhog Day")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hagazussa")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hail Satan?")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Happy Death Day")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hard to Be a God")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Harvey")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Have a Nice Day")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Henry: Portrait of a Serial Killer")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hereditary")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=High Life")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Holiday Heart")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hot Summer Nights")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hotel by the River")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=How to Talk to Girls at Parties")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Hunt for the Wilderpeople")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=I Am Cuba")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=I Am Not a Witch")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=I Am Not Your Negro")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=I, Daniel Blake")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=I, Tonya")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=If Beale Street Could Talk")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=In the Fade")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Indiana Jones and the Last Crusade")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Indignation")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Isle of Dogs")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ixcanul")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Jackie")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Jaws: The Revenge")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Jimi Hendrix Electric Church")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Juliet, Naked")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Jurassic Park")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=K2 and the Invisible Footmen")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Kedi")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Keep Quiet")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Kiki's Delivery Service")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Killer of Sheep")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Labyrinth")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lady Bird")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lady Macbeth")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Landline")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Late Night")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lean on Pete")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Leaning Into the Wind: Andy Goldsworthy")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lemon")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Let the Corpses Tan")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Life, Animated")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lion")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Little Men")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Little Woods")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Liyana")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lo and Behold: Reveries of the Connected World")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Lobster")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Logan")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Long Day's Journey Into Night")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Loving")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Loving Vincent")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Luce")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mad Max: Fury Road")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Madeline's Madeline")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Maiden")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Manchester by the Sea")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mandy")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Maria by Callas")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Marjorie Prime")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Marlina the Murderer in Four Acts")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mary and the Witch's Flower")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mary Magdalene")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mary Queen of Scots")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Maximum Overdrive")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=McKellen: Playing the Part")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Meeting Gorbachev")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Menashe")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mi vida dentro")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mia Madre")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Midsommar")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Minding the Gap")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mirai")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Miss Sharon Jones!")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mississippi Masala")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Monrovia, Indiana")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Monterey Pop")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Monty Python and the Holy Grail")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Moonlight")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Morris from America")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mortal Kombat")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Moses and Aaron")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Mr. Gaga")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Multiple Maniacs")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=My Cousin Rachel")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=My Neighbor Totoro")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Nancy")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=National Theatre Live: Follies")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=National Theatre Live: The Threepenny Opera")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=National Theatre Live: Yerma")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=NausicaÃ¤ of the Valley of the Wind")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Night of the Living Dead")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Nise: The Heart of Madness")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=No Man's Land")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Non-Fiction")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Norman")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Novitiate")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Obit.")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ocean Waves")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Oh Lucy!")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Okko's Inn")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=On the Beach at Night Alone")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=One More Time with Feeling")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=One Week and a Day")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ophelia")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Paddington 2")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Pasolini")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Paterson")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Pavarotti")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Persona")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Pet Sematary")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Phantasm")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Phantom of the Paradise")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Phantom Thread")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Plus One")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Police Story")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Polyester")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Possession")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Prom Night")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Punch-Drunk Love")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Rafiki")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=RBG")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Red Joan")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Retablo")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Revenge")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Robot & Frank")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Rollerball")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Roma")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Rosa Chumbe")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Rosemary's Baby")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Rubber")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ruben Blades Is Not My Name")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Ruben Brandt, Collector")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Santa Sangre")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Satan Bug")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Saving Brinton")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Scarlet Diva")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Science Fair")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Selma")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Shadow")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Shalom Bollywood: The Untold Story of Indian Cinema")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Shoplifters")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Silence")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Skate Kitchen")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Slice")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Solaris")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Sonita")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Sorry to Bother You")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Space Is the Place")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Space Jam")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Speak Up")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Stalker")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Stan")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Stefan Zweig: Farewell to Europe")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Step")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Stop Making Sense")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Studio 54")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Summer 1993")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Summer of 84")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Summer with Monika")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Superman")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Sword of Trust")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=T2 Trainspotting")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tales from the Hood")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tangerine")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Taxi Driver")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tell Them We Are Rising: The Story of Black Colleges and Universities")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Terminal Island")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Aftermath")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Bad Batch")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Beaches of AgnÃ¨s")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Beatles: Eight Days a Week - The Touring Years")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Beguiled")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The BFG")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Big Lebowski")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Big Sick")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Biggest Little Farm")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Bird with the Crystal Plumage")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Black Cat")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Book of Life")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Cakemaker")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Clan")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Clovehitch Killer")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Club")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Dead Don't Die")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Death of Stalin")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Endless")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Exorcist")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Farewell")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Favourite")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Florida Project")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Fog")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Friends of Eddie Coyle")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Gospel According to AndrÃ©")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Grand Budapest Hotel")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Guilty")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Handmaiden")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Handmaid's Tale")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Heiresses")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Hero")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Howling")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Innocents")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Insult")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Killing of a Sacred Deer")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Last Black Man in San Francisco")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Little Hours")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Lost City of Z")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Lovers")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Lure")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Man Who Killed Don Quixote")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Matrix")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Miseducation of Cameron Post")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Mulberry House")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Muppet Christmas Carol")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Night of the Hunter")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Nightingale")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Nutty Professor")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Old Man")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Ornithologist")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2017: Animation")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2017: Documentary")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2017: Live Action")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2018: Animation")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2018: Documentary")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2018: Live Action")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Oscar Nominated Short Films 2019: Live Action")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Party")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Passion of Joan of Arc")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The People vs. Fritz Bauer")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Rocky Horror Picture Show")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Room")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Salesman")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Sandlot")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Second Mother")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Shape of Water")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Texas Chain Saw Massacre")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Texas Chainsaw Massacre 2")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Treasure of the Sierra Madre")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Trip to Spain")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Umbrellas of Cherbourg")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The United States of Autism")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Vessel")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Void")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Wailing")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Wife")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Wound")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Zookeeper's Wife")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Thelma")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=They Shall Not Grow Old")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=This Is Home: A Refugee Story")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Thoroughbreds")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Three Billboards Outside Ebbing, Missouri")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Three Identical Strangers")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tickled")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Time for Ilhan")
return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tito and the Birds")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=To Be or Not to Be")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tom of Finland")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tommy")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Toni Erdmann")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Toni Morrison: The Pieces I Am")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Tony Conrad: Completely in the Present")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Too Late to Die Young")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Transit")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Truth or Dare")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Twin Peaks: Fire Walk with Me")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Twister")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Velvet Goldmine")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Viceroy's House")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Weiner")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Wendy and Lucy")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=What Ever Happened to Baby Jane?")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Whose Streets?")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Wild")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Wild Nights with Emily")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Wildlife")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Willy Wonka & the Chocolate Factory")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Woman at War")

return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Won't You Be My Neighbor?")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Yellow Submarine")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=You Were Never Really Here")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Your Name.")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Zama")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Big Bad Fox and Other Tales...")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=The Gospel According to AndrÃ©")


return_movie_id_BoxOfficeMojo("https://www.boxofficemojo.com/search/?q=Arrival")
'''
#print(arrID)
#df = pd.DataFrame(arrID)
#df.to_csv(r'C:\Users\Solomon\Desktop\movie_id_generate.csv')

df = pd.DataFrame(arrBox)
df.to_csv(r'C:\Users\Solomon\Desktop\movie_box_office__generate.csv')

'''
query = "Viceroy's House"
print(urllib.parse.quote_plus(query))
'''

def get_data_by_title(url):
    response = requests.request("GET", url)
    #df = pd.read_json(response.text)
    #print(df)
    print(response.text)

global df_initial
#df_initial = pd.read_json(r'C:\Users\Solomon\Desktop\Pyg Hack\JSON.py')
#url = "http://www.omdbapi.com/?t=Blaze&apikey=11e7d31d"


def get_data_by_title(url):
    response = requests.request("GET", url)
    df = pd.read_json(response.text)
    #ser = pd.read_json(response.text, typ='series')
    #df = ser.to_frame()
    global df_initial
    df_initial = pd.concat([df_initial,df], sort = True)

#get_data_by_title("http://www.omdbapi.com/?t=2019 Oscar Nominated Short Films: Animation&apikey=11e7d31d")

'''
get_data_by_title("http://www.omdbapi.com/?t=The Big Bad Fox and Other Tales…&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Gospel According to André&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Arrival&apikey=11e7d31d")
'''

'''
##### Movies can't find
get_data_by_title("http://www.omdbapi.com/?t=All-Nite Horror Marathon V&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Amadeus: The Director's Cut&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=An Evening With Linnea Quigley&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Bike Movie Night&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cairo in One Breath&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=CatVideoFest 2018&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deconstructing the Beatles' Sgt. Pepper&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Don’t Look Now&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Femme Frontera Filmmaker Showcase&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Found Footage Festival, Vol. 8&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Found Footage Festival: Cherished Gems&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=George A. Romero Double Feature&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Halloween (1978)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Halloween (2018)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Have A Nice Day (Hao ji le)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=L’Atalante&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Made In Cuba: Short Film Program&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Meeting the Man: James Baldwin in Paris / Ornette: Made in America&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mountainfilm 2019&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Science on Screen: Bombshell: The Hedy Lamarr Story&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Sex Work Activism: Body Politics and Human Rights&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Smart 'n Spooky Kids&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Suspiria (1977)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Suspiria (2018)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The 18th Annual Animation Show of Shows&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The 19th Annual Animation Show of Shows&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Blob (1988)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Nutcracker (NYC Ballet)&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Victoria and Abdul&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Why Don’t You Play in Hell?&apikey=11e7d31d")
'''

############
'''
get_data_by_title("http://www.omdbapi.com/?t=2019 Oscar Nominated Short Films: Animation&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Bread Factory, Part One&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Bread Factory, Part Two&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Faithful Man &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Fantastic Woman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Ghost Story&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Hard Day's Night&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A League of Their Own&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Man Called Ove&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Matter of Life and Death&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Quiet Passion&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A Quiet Place&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=A United Kingdom&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=After Auschwitz&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Akira&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ali: Fear Eats The Soul&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Alien&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Alive and Kicking&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=All Is True&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=All That Heaven Allows&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=All the Queen's Horses&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Amazing Grace&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=American Woman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ancien and the Magic Tablet&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Andrei Rublev&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Anna and the Apocalypse&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Annihilation&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Apollo 11&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Arrival&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ask Dr. Ruth&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=At Eternity's Gate&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Audition&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Batman: The Movie&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Beatriz at Dinner&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Before We Vanish&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Belladonna of Sadness&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Belle De Jour&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Beyond the Valley of the Dolls&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Bicycle Thieves&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Birds of Passage&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Bisbee '17&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Black Clover&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Black Girl&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=BlacKkKlansman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blade&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blade Runner&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blade Runner 2049&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blaze&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blindspotting&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blockers&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Blue Collar&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Bombshell: The Hedy Lamarr Story&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Bones&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Booksmart&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Border&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Boyz n the Hood&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Brain Damage&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Brazil&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Burning&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Butch Cassidy and the Sundance Kid&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Buy Me a Gun&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cafe Society&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Can You Ever Forgive Me?&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Candyman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cape Fear&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Capernaum&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Carmen Jones&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Casablanca&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cemetery Without Crosses&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Certain Women&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Chavela&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Children of Men&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Christine&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Climax&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Close Encounters of the Third Kind&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cold War&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Colossal&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Columbus&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Cooley High&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Crooklyn&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Damsel&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Darkest Hour&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Daughters of the Dust&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dawn of the Dead&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dawson City: Frozen Time&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deconstructing the Beatles' Revolver&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deconstructing the Beatles' White Album&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deconstructing the Beatles: 1963 Yeah! Yeah! Yeah!&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deconstructing the Birth of the Beatles&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Deep Red&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Demon&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Denial&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Destroyer&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dilili in Paris&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dirty Dancing&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Disobedience&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dolores&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Donnie Darko&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Don't Think Twice&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dr. Jekyll and Mr. Hyde&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Dreaming of a Jewish Christmas&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Echo In The Canyon&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=El Mar La Mar&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Elle&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Empire of the Ants&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Endless Poetry&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Eraserhead&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ernest Scared Stupid&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Eugene Onegin&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ex Libris: The New York Public Library&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ex Machina&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Faces Places&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Fanny and Alexander&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Film Stars Don't Die in Liverpool&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Filmworker&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=First Man&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=First Reformed&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Flashdance&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Flower and Sword&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Foreign Body&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Frantz&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Free Solo&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Gadget Girls & ’63 Boycott w/ Risé Sanders-Weir & Gordon Quinn&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ganja & Hess&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Gattaca&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Get Out&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ghost Stories&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Giant Little Ones&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Gimme Danger&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Girlhood&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Grace Jones: Bloodlight and Bami&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Grease&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Gremlins&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Groundhog Day&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hagazussa&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hail Satan?&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Happy Death Day&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hard to Be a God&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Harvey&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Have a Nice Day&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Henry: Portrait of a Serial Killer&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hereditary&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=High Life &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Holiday Heart&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hot Summer Nights&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hotel by the River&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=How to Talk to Girls at Parties&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Hunt for the Wilderpeople&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=I Am Cuba&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=I Am Not a Witch&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=I Am Not Your Negro&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=I, Daniel Blake&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=I, Tonya&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=If Beale Street Could Talk&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=In the Fade&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Indiana Jones and the Last Crusade&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Indignation&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Isle of Dogs&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ixcanul&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Jackie&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Jaws: The Revenge&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Jimi Hendrix Electric Church&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Juliet, Naked&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Jurassic Park&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=K2 and the Invisible Footmen&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Kedi&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Keep Quiet&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Kiki's Delivery Service&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Killer of Sheep&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Labyrinth&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lady Bird&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lady Macbeth&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Landline&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Late Night&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lean on Pete&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Leaning Into the Wind: Andy Goldsworthy&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lemon&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Let the Corpses Tan&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Life, Animated&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lion&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Little Men&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Little Woods&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Liyana&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lo and Behold: Reveries of the Connected World&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Lobster&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Logan&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Long Day's Journey Into Night&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Loving&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Loving Vincent&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Luce&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mad Max: Fury Road&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Madeline's Madeline&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Maiden&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Manchester by the Sea&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mandy&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Maria by Callas&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Marjorie Prime&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Marlina the Murderer in Four Acts&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mary and the Witch's Flower&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mary Magdalene&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mary Queen of Scots&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Maximum Overdrive&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=McKellen: Playing the Part&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Meeting Gorbachev&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Menashe&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mi vida dentro&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mia Madre&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Midsommar&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Minding the Gap&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mirai&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Miss Sharon Jones!&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mississippi Masala&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Monrovia, Indiana&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Monterey Pop&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Monty Python and the Holy Grail&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Moonlight&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Morris from America&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mortal Kombat&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Moses and Aaron&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Mr. Gaga&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Multiple Maniacs&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=My Cousin Rachel&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=My Neighbor Totoro&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Nancy&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=National Theatre Live: Follies&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=National Theatre Live: The Threepenny Opera&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=National Theatre Live: Yerma&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Nausicaä of the Valley of the Wind&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Night of the Living Dead&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Nise: The Heart of Madness&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=No Man's Land&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Non-Fiction &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Norman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Novitiate&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Obit.&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ocean Waves&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Oh Lucy!&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Okko’s Inn&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=On the Beach at Night Alone&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=One More Time with Feeling&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=One Week and a Day&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ophelia&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Paddington 2&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Pasolini&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Paterson&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Pavarotti&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Persona&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Pet Sematary&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Phantasm&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Phantom of the Paradise&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Phantom Thread&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Plus One&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Police Story&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Polyester &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Possession&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Prom Night&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Punch-Drunk Love&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=R.S.&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rafiki&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=RBG&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Red Joan&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Retablo&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Revenge&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Robot & Frank&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rogers Park&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rollerball&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Roma&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rosa Chumbe&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rosemary's Baby&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Rubber&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ruben Blades is Not My Name&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Ruben Brandt, Collector&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Santa Sangre&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Satan & Adam&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Saving Brinton&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Scarlet Diva&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Science Fair&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Selma&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Shadow&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Shalom Bollywood: The Untold Story of Indian Cinema&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Shoplifters&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Silence&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Skate Kitchen&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Slice&apikey=11e7d31d")

get_data_by_title("http://www.omdbapi.com/?t=Solaris&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Sonita&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Sorry to Bother You&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Space is the Place&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Space Jam&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Speak Up&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Stalker&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Stan & Ollie&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Stefan Zweig: Farewell to Europe&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Step&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Stop Making Sense&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Studio 54&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Summer 1993&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Summer of 84&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Summer with Monika&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Superman&apikey=11e7d31d")



get_data_by_title("http://www.omdbapi.com/?t=Sword of Trust&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=T2 Trainspotting&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tales From The Hood&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tangerine&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Taxi Driver&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tell Them We Are Rising: The Story of Black Colleges and Universities&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Terminal Island&apikey=11e7d31d")


get_data_by_title("http://www.omdbapi.com/?t=The Aftermath&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Bad Batch&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Beaches of Agnès&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Beatles: Eight Days a Week - The Touring Years&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Beguiled&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The BFG&apikey=11e7d31d")



get_data_by_title("http://www.omdbapi.com/?t=The Big Lebowski&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Big Sick&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Biggest Little Farm&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Bird with the Crystal Plumage&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Black Cat&apikey=11e7d31d")


get_data_by_title("http://www.omdbapi.com/?t=The Book of Life&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Cakemaker&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Clan&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Clovehitch Killer&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Club&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Dead Don't Die&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Death of Stalin&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Endless&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Exorcist&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Farewell&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Favourite&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Florida Project&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Fog&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Friends of Eddie Coyle&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Gospel According to André&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Grand Budapest Hotel&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Guilty&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Handmaiden&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Handmaid's Tale&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Heiresses&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Hero&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Howling&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Innocents&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Insult&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Killing of a Sacred Deer&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Last Black Man in San Francisco&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Little Hours&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Lost City of Z&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Lovers&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Lure&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Man Who Killed Don Quixote&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Matrix&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Miseducation of Cameron Post&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Mulberry House&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Muppet Christmas Carol&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Night of the Hunter&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Nightingale&apikey=11e7d31d")

get_data_by_title("http://www.omdbapi.com/?t=The Nutty Professor&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Old Man & the Gun&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Ornithologist&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2017: Animation&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2017: Documentary&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2017: Live Action&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2018: Animation&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2018: Documentary&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2018: Live Action&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2019: Documentary&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Oscar Nominated Short Films 2019: Live Action&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Party&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Passion of Joan of Arc&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The People vs. Fritz Bauer&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The River and the Wall&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Rocky Horror Picture Show&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Room&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Salesman&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Sandlot&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Second Mother&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Shape of Water&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Texas Chain Saw Massacre&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Texas Chainsaw Massacre 2&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Treasure of the Sierra Madre&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Trip to Spain&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Umbrellas of Cherbourg&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The United States of Autism&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Vessel&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Void&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Wailing&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Wife&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Wound&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=The Zookeeper's Wife&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Thelma & Louise&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=They Shall Not Grow Old&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=This Is Home: A Refugee Story&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Thoroughbreds&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Three BIllboards Outside Ebbing, Missouri&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Three Identical Strangers&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tickled&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Time for Ilhan&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tito and the Birds&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=To Be Or Not to Be&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Todo el año es navidad&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tom of Finland&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tommy&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Toni Erdmann&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Toni Morrison: The Pieces I am &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Tony Conrad: Completely in the Present&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Too Late to Die Young &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Transit&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Truth or Dare&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Twin Peaks: Fire Walk with Me &apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Twister&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Velvet Goldmine&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Viceroy's House&apikey=11e7d31d")



get_data_by_title("http://www.omdbapi.com/?t=Weiner&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Wendy and Lucy&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=What Ever Happened to Baby Jane?&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Whose Streets?&apikey=11e7d31d")


get_data_by_title("http://www.omdbapi.com/?t=Wild & Scenic Film Festival 2017&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Wild Nights with Emily&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Wildlife&apikey=11e7d31d")

get_data_by_title("http://www.omdbapi.com/?t=Willy Wonka & the Chocolate Factory&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Woman at War&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Won't You Be My Neighbor?&apikey=11e7d31d")

get_data_by_title("http://www.omdbapi.com/?t=Yellow Submarine&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=You Were Never Really Here&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Your Name.&apikey=11e7d31d")
get_data_by_title("http://www.omdbapi.com/?t=Zama&apikey=11e7d31d")
'''

#print(df_initial)
#df_initial.to_csv(r'C:\Users\Solomon\Desktop\movie_with_data_API_working.csv')

'''
url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"page":"1","r":"json","s":"The Lovers"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "7a74a7fff7mshcd10438e32c455ap11897fjsnbb321ee4d3da"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

'''

df_movie_data_kaggle = pd.read_csv(filepath_or_buffer = r'C:\Users\Solomon\Desktop\Pyg Hack\the_movies_dataset\movies_metadata.csv')
df_pyg_event_sales = pd.read_csv(r'C:\Users\Solomon\Desktop\Pyg Hack\PygArtHackTheater2019\datasets\gross_revenue_by_event.csv', encoding='cp1252')
df = df_movie_data_kaggle.set_index('original_title').join(df_pyg_event_sales.set_index('original_title'))
df = df.dropna(subset=['Gross Revenue'])

#df.to_csv(r'C:\Users\Solomon\Desktop\movie_with_data.csv')
#print(df)


df_movie_data_DW = pd.read_csv(filepath_or_buffer = r'C:\Users\Solomon\Desktop\Pyg Hack\movie_metadata.csv')
df_pyg_event_sales = pd.read_csv(r'C:\Users\Solomon\Desktop\Pyg Hack\PygArtHackTheater2019\datasets\gross_revenue_by_event.csv', encoding='cp1252')
df = df_movie_data_DW.set_index('original_title').join(df_pyg_event_sales.set_index('original_title'))
df = df.dropna(subset=['Gross Revenue'])

#df.to_csv(r'C:\Users\Solomon\Desktop\movie_with_data_new.csv')
#print(df)
#tp = pd.read_csv(r'C:\Users\Solomon\Desktop\Pyg Hack\name.basics.tsv\data.tsv',sep='\t', header=None, chunksize=1000)
#df = pd.concat(tp, ignore_index=True)







