Title: Unnamed Tower Defense Game Part 1: Inspiration and Concept
Date: 2025-03-09
Category: Game Dev
Authors: LlamaSE
Tags: game dev, godot, tower defense, programming

For a long time I've been trying to get more serious about Game Dev and coming up with a game project that is:

- Possible for me to develop solo with my current skills as a programmer (professional) and artist (bad)
- Interesting enough to keep me engaged with the process
- Actually marketable and fun
- Small enough in scope that I can make it in a reasonable timeframe

Pretty much every other concept I've come up with has serious problems with the latter point. The games that I most enjoy playing myself are strategy focused so I often find myself pointed in that direction when coming up with ideas. The problem with this is that systems-heavy strategy games are some of the most time consuming to develop so if I want to develop a game that holds my interest but won't take a decade I need to make a compromise.

### Primary Inspiration

I spent a lot of time in middle and high school playing RTS games with my friends before *League of Legends* came onto the scene and grabbed our attention. Most of all I really enjoyed playing *Starcraft I and II* and *Warcraft III.* In the years before *Starcraft II's* release I was particularly grabbed by Warcraft 3 custom maps and especially tower defense maps. Some of the more popular tower defense maps from *War3* like *Legion TD* and *Element TD* went on to eventually be made as full standalone game releases by passionate developers while others like *Gem TD* never saw a commercial release but were recreated in *Starcraft II* and *Dota 2* (another Warcraft 3 custom map that eventually saw widespread commercial success).

One map that I have always found compelling was [Poker TD](https://www.epicwar.com/maps/326012/). The concept was simple: every round you would construct 5 buildings, each one representing a card from a poker hand. Depending on the hand you were dealt, you would then combine the buildings into a single tower that would gain strength and abilities based on the rank of the poker hand as well as the highest card of the hand. You also gained gold from killing enemies that could be used to "tip" your dealer, giving you a higher chance of being dealt a strong hand. This one-note gameplay doesn't really hold up to modern standards but it was a fun map to play once or twice. If you're interested you can go [here](https://www.youtube.com/watch?v=afjqy6nvbZE) to see the map being played by WTii. 

The map has seen a couple more recent iterations over the years including one released in the *Starcraft II* arcade that made use of a unit combining mechanic and mazing. There's also *Poker Tower Defense* by BelindaMakesGames which can be found [here](https://belindamakesgames.itch.io/poker-tower-defense). I appreciated their modern take and thought the hand manipulation mechanics were cool but didn't like that you were forced to watch ads to get access to more uses of them (typical bad mobile game design). I also didn't find what little meta progression was present very compelling. They were obviously constrained by the timeframe of game jam development and mobile-centric design but I still found the concept interesting to play even years later. 

A few years ago when I was thinking up ideas that I could make the poker-based tower defense concept kept coming back to my mind. I felt like I could make a good attempt using the basic poker mechanic while applying others from roguelite and autobattler games to make something well-rounded and fun. Tower defense as a genre is also complex enough to keep me engaged while avoiding some complexities of the types of games tower defense is derived from like RTS.

### Other Inspirations

With the poker mechanic in mind I started thinking about what I could do to spice up the formula, so I drew on some of my favorite indie games of the past 5 years for inspiration. I really liked Die of Death Games' *Rogue Tower* (link [here](https://store.steampowered.com/app/1843760/Rogue_Tower/)). The idea of applying roguelite mechanics to a Tower Defense, to my knowledge, hadn't really been tried up to that point and I thought it was a really solid first execution. I enjoyed the variety of strategies you could employ but found the meta-progression to be very front-loaded, with the upgrade tree that lets you choose upgrades more often being an order of magnitude more powerful than every other. I thought the mechanic for building the map as you went was cool in theory but in practice resulted in obnoxiously large maps that made waves take a really long time with lots of map space going unused by your towers.

On the autobattler end I really enjoyed [SNKRX](https://store.steampowered.com/app/915310/SNKRX/) by a327ex. I loved the incredibly simple concept and thought that the autobattler synergies and upgrade system were really well designed. I've also taken some inspiration from [Teamfight Tactics](https://teamfighttactics.leagueoflegends.com/en-us/) especially in building a modular upgrade system.

### Addressing the Flaws

With the concept in mind I started brainstorming ways to make a well rounded game. Going all the way back to the original map, none of the takes made you care about the **suits** of the cards that you're playing, only the rank of the cards and the rank of the hands that the cards comprise. What I landed on was the idea of having "Suit Powers" which confer an ability to the tower that is themed after the object that the card suit represents. I realized that the suit power system might be confusing when you are being dealt hands that comprise cards from multiple suits so I settled on having meters that fill up whenever you "play" a card from the corresponding suit. Play 10 cards from a single suit and you get an upgrade for that suit that you can apply to a tower of your choice. I also realized the potential that suit powers had in adding to replayability so I brainstormed up a bunch of different suits based playing and tarot card suits from various world cultures as well as a few of my own ideas. The idea is that you would choose a deck "loadout" of 4 suits before each run/level. I also wanted a RPS-like damage system to encourage diverse loadouts so each suit has a damage type associated with it.

![Photo]({attach}suits.png)

I thought the hand manipulation mechanics from BelindaMakesGames' *Poker Tower Defense* were great despite the mobile-centric design so I settled on tying these powers to a currency system that would also be used to purchase upgrades from a typical roguelike-esq shop. On the note of upgrades, I decided pretty early on that I wanted two different kinds of upgrades, modular upgrades that are applied to a specific tower and global upgrades that affect all towers, a subset of towers or some other aspect of gameplay. An upgrade is selected from 3 every round with more being available in the previously-mentioned shop. Both types of upgrades can be ranked up for a stronger effect. Each tower would have 3 "slots" for modular upgrades with a 4th special slot reserved for suit powers.

This all sounds like a lot, especially coming from the simple mechanics of the original inspiration but I think I've done a decent job so far of managing scope creep. At time of writing I've been working on the game for a little less than a year including some pretty massive periods of inacivity so we still have quite a ways to go but I hope you'll enjoy reading about my process.

Join me next time as I discuss finding an art style that I can execute with absolutely 0 talent as an artist.

[Part 2]({filename}../part2/part2.md)
