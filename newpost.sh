#!/bin/bash
set -e

cleanup() {
  clearf
}

clearf() {
  printf $(tput sgr0)
}

trap cleanup EXIT

FN=$(ls -ct sources/ | head -n1)

echo Found new blog post "$(tput smul)$FN$(tput sgr0)"
read -p " - Is that the right filename ($(tput setaf 2)y$(tput sgr0)/$(tput setaf 1)n$(tput sgr0))? $(tput bold)" right
clearf

if [ $right != "y" ]
then
  read -p "   - Correct file name: $(tput bold)" FN
  clearf
fi
read -p "Title of blog post: $(tput bold)" TITLE
clearf

DAY="$(date +%d)"
MONTH="$(date +%B)"
YEAR="$(date +%Y)"

read -p "Is this the correct date $(tput smul)$DAY $MONTH, $YEAR$(tput rmul) ($(tput setaf 2)y$(tput sgr0)/$(tput setaf 1)n$(tput sgr0))? $(tput bold)" yn
clearf

if [ $yn != "y" ]
then
  read -p " - Is the year correct($(tput setaf 2)y$(tput sgr0)/$(tput setaf 1)n$(tput sgr0))? $(tput bold)" yn
  clearf
  if [ $yn != "y" ]
  then
    read -p "   - Year? $(tput bold)" YEAR
    clearf
  fi
  read -p " - Is the month correct($(tput setaf 2)y$(tput sgr0)/$(tput setaf 1)n$(tput sgr0))? $(tput bold)" yn
  clearf
  if [ $yn != "y" ]
  then
    read -p "   - Month? $(tput bold)" MONTH
    clearf
  fi
  read -p " - Is the day correct($(tput setaf 2)y$(tput sgr0)/$(tput setaf 1)n$(tput sgr0))? $(tput bold)" yn
  clearf
  if [ $yn != "y" ]
  then
    read -p "   - Day? $(tput bold)" DAY
    clearf
  fi
fi

echo

echo Appending "$(tput bold)$FN:$TITLE$(tput sgr0)" to "$(tput bold)sources/order.txt$(tput sgr0)"
echo "$FN:$TITLE" >> sources/order.txt

echo

FILEMONTH=$(tail -r calendar/order.txt | grep -m1 "^-" | sed "s/^-//")
FILEYEAR=$(tail -r calendar/order.txt | grep -m1 "^*" | sed "s/^*//")

if [ $YEAR != $FILEYEAR ]
then
  echo "Appending $(tput bold)*$YEAR$(tput sgr0) to $(tput bold)calendar/order.txt$(tput sgr0)"
  echo "*$YEAR" >> calendar/order.txt
fi

if [ $MONTH != $FILEMONTH ]
then
  echo "Appending $(tput bold)-$MONTH$(tput sgr0) to $(tput bold)calendar/order.txt$(tput sgr0)"
  echo "*$MONTH" >> calendar/order.txt
fi

echo Appending "$(tput bold)$TITLE:$(echo $FN | sed "s/tex/html/g"):$DAY$(tput sgr0)" to "$(tput bold)calendar/order.txt$(tput sgr0)"
echo "$TITLE:$(echo $FN | sed "s/tex/html/g"):$DAY" >> calendar/order.txt

echo

echo Running make...

make

echo Running git commands

git add .
git commit -m "Posted new blog post"
git push

cleanup
