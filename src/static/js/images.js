let currentIndex = 0;
function transitionImage(forward) {
  const newIndex =
    (currentIndex + (forward ? 1 : -1) + images.length) % images.length;

  imageObj = images[newIndex];
  const image = document.getElementById("mainImage");
  image.src = imageObj.filepath;
  const description = document.getElementById("imageDescription");
  if (!imageObj.tooltip) {
    description.removeAttribute("data-tooltip");
  } else {
    description.setAttribute("data-tooltip", imageObj.tooltip);
  }
  description.innerHTML = imageObj.caption;

  currentIndex = newIndex;

  const imageWrapper = document.getElementById("mainImageWrapper");

  image.style.visibility = "hidden";
  imagesLoaded(imageWrapper, function () {
    image.style.visibility = "inherit";
  });

  return false;
}

const images = [
  {
    // This image should always be first
    imageDescriptionId: "imageDescription-18042022",
    filepath: "static/assets/dancing_image.jpg",
    tooltip: "",
    caption: "",
  },
  {
    filepath: "static/assets/team/2022_09_11.jpg",
    tooltip: "",
    caption: "DM2 2022 Champions",
  },
  {
    filepath: "static/assets/team/19A_00096.jpg",
    tooltip: "",
    caption: "Elite Invite 2022 Champions",
  },
  {
    imageDescriptionId: "imageDescription-08092019",
    filepath: "static/assets/team/2019-08-09-DM-Aachen.jpg",
    tooltip:
      "hinten: Sylwester, Basti, Julian, Leo, Steven, Caspar, Arne, Nick, Vlad, Phil, Hartley, Paul R. - vorne: Schuie, Clemens, Lucas, Ron, Tom, Joel, Thore, Taylor, Christian, Yannis, Marky",
    caption: "Deutsche Meisterschaften 1. Liga in Aachen 08.09.2019",
  },
  {
    imageDescriptionId: "imageDescription-09092018",
    filepath: "static/assets/team/2018-09-09-DM-Kiel.jpg",
    tooltip:
      "hinten: Julian, Jonah, Vlad, Marv, Phil, Nick, Tom, Felix, Sylwester, Steven - vorne: Marv A., Ron, Basti, Fabi, Christian, Paul, Tom, Chente",
    caption: "Deutsche Meisterschaften 1. Liga in Kiel 09.09.2018",
  },
  {
    imageDescriptionId: "imageDescription-03092017",
    filepath: "static/assets/team/2017-09-03-DM-Duesseldorf.jpg",
    tooltip:
      "hinten: Vlad, Sylwester, Josi, Paul, Joseph, Caspar, Lukas, Cardi, Leo, Marv, Phil, Christian - vorne: Chente, Ron, Paul, Paul, Joel, Basti, Martin, Julian, Richard, Steven, Tom, Nick",
    caption: "Deutsche Meisterschaften 1. Liga in Duesseldorf 03.09.2017",
  },
  {
    imageDescriptionId: "imageDescription-24072016",
    filepath: "static/assets/team/2016-07-24-AReliII-Muenchen.jpg",
    tooltip:
      "hinten: Leo, Piotr, Phil, Thore, Jonas, Lukas, Joscha, Daniel, Tom, Joseph, Lars, Christian - vorne: Martin, Ron, Bas, Dense, Marcus, Julian, Richi, Steven, Philipp, Francesco",
    caption: "A-Relegation zur Deutschen Meisterschaft 2. WE in 0 24.07.2016 ",
  },
  {
    imageDescriptionId: "imageDescription-18092015",
    filepath: "static/assets/team/2015-09-18-DM-Kassel.jpg",
    tooltip:
      "hinten: Alf, Jos, Lukas, Daniel, Dense, Bas, Stefan, Ron, Martin, Phil, Filip - vorne: Jonas, Leo, Christian, Richi, Julius, Julian, Lars, Steven, Joscha",
    caption: "Deutsche Meisterschaften 1. Liga in Kassel 18.09.2015 ",
  },
  {
    imageDescriptionId: "imageDescription-19042015",
    filepath: "static/assets/team/2015-04-19-HH-Rumble-Hamburg.jpg",
    tooltip:
      "hinten: Stefan, Lars, Leo, Steven, Dense, Lukas, Alf, Martin - vorne: Julian, Jonas, Daniel, Bas, Joscha, Jos",
    caption: "HH Rumble in Hamburg 19.04.2015 ",
  },
  {
    imageDescriptionId: "imageDescription-13072014",
    filepath: "static/assets/team/2014-07-13-AReli2-Muenchen.jpg",
    tooltip:
      "Ron, Filip, Steven, Bas, Alois, Daniel, Stefan, Julian, Julius, Lukas, Joscha, Dennis, Hammer, Odse, Alfons, Lars, Richi",
    caption: "2. A-Relegation in Muenchen 13.07.2014",
  },
  {
    imageDescriptionId: "imageDescription-12042014",
    filepath: "static/assets/team/2014-04-12-HH-Rumble-Hamburg.jpg",
    tooltip:
      "hinten: Hammer, Julian, Tom, Bruno, Lukas, Joseph, Stefan, Benjamin - mitte: Bas, Richi, Alois, Joscha, Bernd, Julius - vorne: Odse, Ron, Marco, Alfons, Jos, Flow",
    caption: "HH Rumble in Hamburg 12.04.2014",
  },
  {
    imageDescriptionId: "imageDescription-02032014",
    filepath: "static/assets/team/2014-03-02-DM-Heidelberg.jpg",
    tooltip:
      "hinten: Bernd, Joscha, Bruno, Julian, Benjamin - vorne: Ron, Lars, Alf, Richi",
    caption: "DM 1. Liga Indoor - 2. Spieltag in Heidelberg 02.03.2014",
  },
  {
    imageDescriptionId: "imageDescription-25012014",
    filepath: "static/assets/team/2014-01-25-IDM14-Potsdam.jpg",
    tooltip:
      "hinten: Bruno, Joscha, Lukas, Benjamin, Julian, Bernd - vorne: Ali, Richi, Alf, Lars, Ron",
    caption: "DM 1. Liga Indoor - 1. Spieltag in Potsdam 25.01.2014",
  },
  {
    imageDescriptionId: "imageDescription-11012014",
    filepath: "static/assets/team/2014-01-11-Mudders-Cup-Bremen.jpg",
    tooltip: "hinten: Joscha, Julian, Lukas - vorne: Ron, Alf, Richi",
    caption: "Mudders Cup in Bremen 11.01.2014",
  },
  {
    imageDescriptionId: "imageDescription-15092013",
    filepath: "static/assets/team/2013-09-15-DM-Frankfurt.gif",
    tooltip:
      "hinten: Mike, Joscha, Daniel, Stefan, Lukas, Julius, Falko, Ali, Bas - vorne: Raz, Andres, Lars, Dave, Dense, Ben, Alfons, Richi, Ron",
    caption: "DM 1. Liga in Frankfurt 15.09.2013 ",
  },
  {
    imageDescriptionId: "imageDescription-13072013",
    filepath: "static/assets/team/2013-07-13-AReli2-Rappenau.jpg",
    tooltip:
      "hinten: Stefan, Mike, Bas, Julius, Joscha, Ali, Lukas, Falko, Ben, Richi - vorne: Ron, Dave, Dense, Lars, Daniel, Andres, Raz",
    caption: "2. A-Relegation in Bad Rappenau 13.07.2013",
  },
  {
    imageDescriptionId: "imageDescription-23062013",
    filepath: "static/assets/team/2013-06-23-Quali-Hannover.jpg",
    tooltip:
      "hinten: Mirko, Nicolo, Bernd, Falk, Guido, Odse, Hammer - vorne: Joshua, Jan, Flo, Simon, Alois",
    caption: "Quali Nord in Hannover 23.06.2013",
  },
  {
    imageDescriptionId: "imageDescription-22062013",
    filepath: "static/assets/team/2013-06-22-AReli1-Berlin.jpg",
    tooltip:
      "hinten: Ron, Dave, Richi, Alfons, Lars, Raz, Ben, Bas - vorne: Julius, Mike, Lukas, Dense, Ali, Joscha, Stefan, Daniel, Andres",
    caption: "1. A-Relegation in Berlin 22.06.2013",
  },
  {
    imageDescriptionId: "imageDescription-15062013",
    filepath: "static/assets/team/2013-06-15-Amsterdam.jpg",
    tooltip:
      "hinten: Ben, Bas, Russ, Niko, Daniel, Dave, Lars, Joscha, Hammer - vorne: Mike, Julius, Lukas, Stefan, Dense, Bernd, Alfons",
    caption: "Windmill Windup in Amsterdam 15.06.2013",
  },
  {
    imageDescriptionId: "imageDescription-01062013",
    filepath: "static/assets/team/2013-06-01-DDC-Koeln.jpg",
    tooltip:
      "hinten: Lukas, Nicolo, David, Joshua, Mike, Dave - vorne: Joscha, Ron, Alfons, Flow, Niko, Richi",
    caption: "DDC in Koeln 01.06.2013",
  },
  {
    imageDescriptionId: "imageDescription-19052013",
    filepath: "static/assets/team/2013-05-19-BUM.jpg",
    tooltip:
      "hinten: Joscha, Ron, Bas, Dense, Bernd - vorne: Richi, Stefan, Daniel, Julius, Mike",
    caption: "BUM in Berlin 19.05.2013",
  },
  {
    imageDescriptionId: "imageDescription-14042013",
    filepath: "static/assets/team/2013-04-14-HH-Rumble.jpg",
    tooltip:
      "hinten: Lukas, Julius, David, Hammer, Bernd, Daniel, Stefan, Dave, Joscha, Falko, Nicolo - vorne: Mike, Ron, Raz, Dennis, Bas, Lars, Russ, Ben, Richi",
    caption: "HH Rumble in Hamburg 14.04.2013",
  },
  {
    imageDescriptionId: "imageDescription-24022013",
    filepath: "static/assets/team/2013-02-24-DM_Berlin.jpg",
    tooltip:
      "hinten: Joscha, Bas, Lars, Lukas, Falk - vorne: Hammer, Richi, Raz, Julius, Ron",
    caption: "DM 2. Liga Indoor in Berlin 24.02.2013",
  },
  {
    imageDescriptionId: "imageDescription-20012013",
    filepath: "static/assets/team/2013-01-20-Karlsruhe.jpg",
    tooltip:
      "hinten: Hammer, Bernd, Lukas, Joscha, Richi - vorne: Lars, Raz, Bas, Falk",
    caption: "B-Reli Indoor in Karlsruhe 20.01.2013",
  },
  {
    imageDescriptionId: "imageDescription-12012013",
    filepath: "static/assets/team/2013-01-13-Bremen.jpg",
    tooltip:
      "hinten: Lars, Bernd, Lukas, Joscha, Hammer - vorne: Bas, Ron, Richi, Raz",
    caption: "Mudders Cup in Bremen 12.01.2013",
  },
  {
    imageDescriptionId: "imageDescription-15092012",
    filepath: "static/assets/team/2012-09-15-Frankfurt.jpg",
    tooltip:
      "hinten: Alfons, Hammer, Falk, Bernd, Dennis, Stefan, Bas, Thomas, Ben, Bruno, Marco - vorne: Lars, Richi, Sergej, Dave, Jan, Daniel, Ron, Russ, Raz",
    caption: "DM 2. Liga in Frankfurt 15.09.2012",
  },
  {
    imageDescriptionId: "imageDescription-09062012",
    filepath: "static/assets/team/2012-06-09-DDC.jpg",
    tooltip:
      "hinten: Ben, Hammer, Jan B., Joni, Bernd, Dennis, Jan F., Falk, Marco - vorne: Raz, Ron, Daniel, Dave, Richi, Lars, Bas, Bruno",
    caption: "DDC in Koeln 09.06.2012",
  },
  {
    imageDescriptionId: "imageDescription-09102011",
    filepath: "static/assets/team/2011-10-09-BBM-Berlin.jpg",
    tooltip:
      "hinten: Jan, Timothy, Ben, Falk, Ron, Scottie, Daniel, Nicolo - vorne: Bas, Raz, Russ, Dave, Marco",
    caption: "Berlin-Brandenburg Meisterschaft in Berlin 09.10.2011",
  },
  {
    imageDescriptionId: "imageDescription-01082010",
    filepath: "static/assets/team/2010-08-01-DM-Jena.jpg",
    tooltip: "Dense, Bernd, Falko, Russ, Jan B., ?, Jan F.",
    caption: "Deutsche Meisterschaft 2. Liga in Jena 01.08.2010",
  },
  {
    imageDescriptionId: "imageDescription-03072010",
    filepath: "static/assets/team/2010-07-03-WUCC-Prag.jpg",
    tooltip:
      "hinten: Tim, ?, ?, Theo, Thomas, Tobi, Gili, Ralle, Juv, ?, Scottie, Falko - vorne: ?, ?, Graham, Micha, Blümchen, Lars, Jost, Markus",
    caption: "WUCC - Masters in Prag 03.07.2010",
  },
  {
    imageDescriptionId: "imageDescription-24092009",
    filepath: "static/assets/team/2009-09-24-XEUCF-London.jpg",
    tooltip:
      "hinten: Daniel, Jan, ?, Jakob, ?, Lukas, Dense, Matze, Ragnar, Bruno, Bastian - vorne: Thomas, Tim, Markus, ?, Raz, Falko, ?",
    caption: "XEUCF in London 24.09.2009",
  },
  {
    imageDescriptionId: "imageDescription-28082009",
    filepath: "static/assets/team/2009-08-28-EUCR-Nuernberg.jpg",
    tooltip:
      "hinten: ?, ?, Dense, Bastian, Ralle, Jakob, ?, ?, ?, Lukas, bruno, Tobi, Jan, ?, Falko - vorne: Markus, Raz, Tim, ?",
    caption: "EUCR - East in Nuernberg 28.08.2009",
  },
  {
    imageDescriptionId: "imageDescription-14082009",
    filepath: "static/assets/team/2009-08-14-DM-Koeln.jpg",
    tooltip:
      "hinten: Lukas, Glenn, Falko, Tobi, Ralle, Ben - vorne: Jakob, Bruno, ?, ?, Raz, ?, Dense, ?, ?",
    caption: "Deutsche Meisterschaft - 2. Liga in Koeln 14.08.2009",
  },
  {
    imageDescriptionId: "imageDescription-",
    filepath: "static/assets/team/19xx-xx-xx-xx4.jpg",
    tooltip:
      "hinten: Adrian, ?, Ossi, Tobias, Gerd - vorne: Holger, Jens, Manni, Knut",
    caption: "Bild4 in ? xx.xx.19xx",
  },
  {
    imageDescriptionId: "imageDescription-",
    filepath: "static/assets/team/19xx-xx-xx-xx3.jpg",
    tooltip: "Flo, Gerd, Acki, Knut",
    caption: "Bild3 in Rothenburg? xx.xx.19xx",
  },
  {
    imageDescriptionId: "imageDescription-",
    filepath: "static/assets/team/19xx-xx-xx-xx2.jpg",
    tooltip: "Ossi, Adrian, Holger, Flo, Jens",
    caption: "Bild2 in ? xx.xx.19xx",
  },
  {
    imageDescriptionId: "imageDescription-",
    filepath: "static/assets/team/19xx-xx-xx-xx1.jpg",
    tooltip: "Gerd, Norbert, Tobias, Holger, Knut, Manni, Ossi, Flo",
    caption: "Bild1 in ? ?.?.19xx",
  },
  {
    imageDescriptionId: "imageDescription-27071997",
    filepath: "static/assets/team/1997-07-27-Vancouver.jpg",
    tooltip:
      "hinten: Jost, Adrian, Fabs, Manni, Holger - mitte: ?, Ossi, Nick, Markus, Fred, Juhv - vorne: ?, Flo Pfender, Flo Beiglboeck, Jens, Knut, Theo",
    caption: "WUCC in Vancouver 27.07.1997",
  },
];
