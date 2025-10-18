
import string
import random


# take letter guess from the user function
def letter_guess():
    while True:
        result = input("Please choose a letter: ").lower()

        # check if the letter was valid
        if result in string.ascii_lowercase and len(result) == 1:
            return result
        else:
            print("Please choose a valid letter or ensure only one letter is chosen")

# prompt user to solve or guess another letter function


def solve_or_guess():
    while True:
        try:
            result = int(input("""Would you like to solve or guess a letter? \n
                            1. Solve \n
                            2. Guess a letter \n """))
            return result
        except:
            print("Please enter either 1 or 2")


# lots of random words for the machine to choose randomly from
word_list = "about, above, abuse, accept, accident, accuse, across, activist, actor, administration, admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, ancient, anger, animal, anniversary, announce, another, answer, apologise, appeal, appear, appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, colony, color, combine, command, comment, committee, common, communicate, community, company, compare, compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner, diplomat, direct, direction, disappear, disarm, disaster, discover, discrimination, discuss, disease, dismiss, dispute, dissident, distance, divide, doctor, document, dollar, donate, double, dream, drink, drive, drown, during, early, earth, earthquake, ecology, economy, education, effect, effort, either, elect, electricity, embassy, embryo, emergency, emotion, employ, empty, enemy, energy, enforce, engine, engineer, enjoy, enough, enter, environment, equal, equipment, escape, especially, establish, estimate, ethnic, evaporate, event, every, evidence, exact, examine, example, excellent, except, exchange, excuse, execute, exercise, exile, exist, expand, expect, expel, experience, experiment, expert, explain, explode, explore, export, express, extend, extra, extraordinary, extreme, extremist, factory, false, family, famous, father, favourite, federal, female, fence, fertile, field, fierce, fight, final, financial, finish, fireworks, first, float, flood, floor, flower, fluid, follow, force, foreign, forest, forget, forgive, former, forward, freedom, freeze, fresh, friend, frighten, front, fruit, funeral, future, gather, general, generation, genocide, gentle, glass, goods, govern, government, grain, grass, great, green, grind, ground, group, guarantee, guard, guerrilla, guide, guilty, happen, happy, harvest, headquarters, health, heavy, helicopter, hijack, history, holiday, honest, honor, horrible, horse, hospital, hostage, hostile, hotel, house, however, human, humor, hunger, hurry, husband, identify, ignore, illegal, imagine, immediate, immigrant, import, important, improve, incident, incite, include, increase, independent, individual, industry, infect, inflation, influence, inform, information, inject, injure, innocent, insane, insect, inspect, instead, instrument, insult, intelligence, intelligent, intense, interest, interfere, international, Internet, intervene, invade, invent, invest, investigate, invite, involve, island, issue, jewel, joint, judge, justice, kidnap, knife, knowledge, labor, laboratory, language, large, laugh, launch, learn, leave, legal, legislature, letter, level, liberal, light, lightning, limit, liquid, listen, literature, little, local, lonely, loyal, machine, magazine, major, majority, manufacture, march, market, marry, material, mathematics, matter, mayor, measure, media, medicine, member, memorial, memory, mental, message, metal, method, microscope, middle, militant, military, militia, mineral, minister, minor, minority, minute, missile, missing, mistake, model, moderate, modern, money, month, moral, morning, mother, motion, mountain, mourn, movement, movie, murder, music, mystery, narrow, nation, native, natural, nature, necessary, negotiate, neighbor, neither, neutral, never, night, noise, nominate, normal, north, nothing, nowhere, nuclear, number, object, observe, occupy, ocean, offensive, offer, office, officer, official, often, operate, opinion, oppose, opposite, oppress, orbit, order, organize, other, overthrow, paint, paper, parachute, parade, pardon, parent, parliament, partner, party, passenger, passport, patient, peace, people, percent, perfect, perform, period, permanent, permit, person, persuade, physical, physics, picture, piece, pilot, place, planet, plant, plastic, please, plenty, point, poison, police, policy, politics, pollute, popular, population, position, possess, possible, postpone, poverty, power, praise, predict, pregnant, present, president, press, pressure, prevent, price, prison, private, prize, probably, problem, process, produce, profession, professor, profit, program, progress, project, promise, propaganda, property, propose, protect, protest, prove, provide, public, publication, publish, punish, purchase, purpose, quality, question, quick, quiet, radar, radiation, radio, railroad, raise, reach, react, ready, realistic, reason, reasonable, rebel, receive, recent, recession, recognize, record, recover, reduce, reform, refugee, refuse, register, regret, reject, relations, release, religion, remain, remains, remember, remove, repair, repeat, report, represent, repress, request, require, rescue, research, resign, resist, resolution, resource, respect, responsible, restaurant, restrain, restrict, result, retire, return, revolt, right, river, rocket, rough, round, rubber, rural, sabotage, sacrifice, sailor, satellite, satisfy, school, science, search, season, second, secret, security, seeking, seize, Senate, sense, sentence, separate, series, serious, serve, service, settle, several, severe, shake, shape, share, sharp, sheep, shell, shelter, shine, shock, shoot, short, should, shout, shrink, sickness, signal, silence, silver, similar, simple, since, single, sister, situation, skeleton, skill, slave, sleep, slide, small, smash, smell, smoke, smooth, social, soldier, solid, solve, sound, south, space, speak, special, speech, speed, spend, spill, spirit, split, sport, spread, spring, square, stand, start, starve, state, station, statue, steal, steam, steel, stick, still, stone, store, storm, story, stove, straight, strange, street, stretch, strike, strong, structure, struggle, study, stupid, subject, submarine, substance, substitute, subversion, succeed, sudden, suffer, sugar, suggest, suicide, summer, supervise, supply, support, suppose, suppress, surface, surplus, surprise, surrender, surround, survive, suspect, suspend, swallow, swear, sweet, sympathy, system, target, taste, teach, technical, technology, telephone, telescope, television, temperature, temporary, tense, terrible, territory, terror, terrorist, thank, theater, theory, there, these, thick, thing, think, third, threaten, through, throw, tired, today, together, tomorrow, tonight, torture, total, touch, toward, trade, tradition, traffic, tragic, train, transport, transportation, travel, treason, treasure, treat, treatment, treaty, trial, tribe, trick, troops, trouble, truce, truck, trust, under, understand, unite, universe, university, unless, until, urgent, usual, vacation, vaccine, valley, value, vegetable, vehicle, version, victim, victory, video, village, violate, violence, visit, voice, volcano, volunteer, wages, waste, watch, water, wealth, weapon, weather, weigh, welcome, wheat, wheel, where, whether, which, while, white, whole, willing, window, winter, withdraw, without, witness, woman, wonder, wonderful, world, worry, worse, worth, wound, wreck, wreckage, write, wrong, yellow, yesterday, young"
word_list = word_list.replace(" ", "")
word_list = word_list.split(",")


# hangman states (hs)

hs_0 = ""

hs_1 = "_________"

hs_2 = """
          |
          |
          |
          |
          |
          |
          |
          |
          |_________"""

hs_3 = """
           _________
          |/
          |
          |
          |
          |
          |
          |
          |
          |_________"""

hs_4 = """
           _________
          |/   |
          |    |
          |
          |
          |
          |
          |
          |
          |_________"""

hs_5 = """
           _________
          |/   |
          |    |
          |    O
          |
          |
          |
          |
          |
          |_________"""

hs_6 = """
           _________
          |/   |
          |    |
          |    O
          |    |
          |    |
          |
          |
          |
          |_________"""

hs_7 = """
           _________
          |/   |
          |    |
          |    O
          |   /|
          |    |
          | 
          |
          |
          |_________"""

hs_8 = """
           _________
          |/   |
          |    |
          |    O
          |   /|\\
          |    |
          | 
          |
          |
          |_________"""

hs_9 = """
           _________
          |/   |
          |    |
          |    O
          |   /|\\
          |    |
          |   /
          |
          |
          |_________"""

hs_10 = """
           _________
          |/   |
          |    |
          |    O
          |   /|\\
          |    |
          |   / \\
          |
          |
          |_________"""

hangman_states = [hs_0, hs_1, hs_2, hs_3,
                  hs_4, hs_5, hs_6, hs_7, hs_8, hs_9, hs_10]


# choose a random word from list
hangman_word = random.choice(word_list)


# initialise set for guessed letters, guess counter, life counter and current word state
guessed_letters = set()
lives_remaining = 10
guess_counter = 0
current_word_state = len(hangman_word) * "_"

current_hangman_state = hangman_states[0]

# initialise game loop
while True:

    # check number of lives remaining
    if lives_remaining > 0:

        # check if user has guessed all letters without solving
        if current_word_state == hangman_word:
            guess_counter += 1
            current_hangman_state = hangman_states[10-lives_remaining]
            print("#################################################")
            print(
                f"Correct! The word was {hangman_word}. you guessed it in {guess_counter} guesses!")
            print(current_hangman_state)
            break
        else:

            # ask user if they want to solve or guess another letter
            print(
                f"The word is currently: {current_word_state} of length {len(hangman_word)}")
            solve = solve_or_guess()
            if solve == 1:

                # get users solve attempt
                solve_attempt = input("What is your guess?: ").lower()

                # compare with hangman word
                if solve_attempt == hangman_word:
                    guess_counter += 1
                    current_hangman_state = hangman_states[10-lives_remaining]
                    print("#################################################")
                    print(
                        f"Correct! The word was {hangman_word}. you guessed it in {guess_counter} guesses!")
                    print(current_hangman_state)
                    break

                else:
                    lives_remaining -= 1
                    guess_counter += 1
                    current_hangman_state = hangman_states[10-lives_remaining]
                    print("#################################################")
                    print("Incorrect guess")
                    print(f"You have {lives_remaining} lives left")
                    print(current_hangman_state)

            elif solve == 2:

                while True:

                    # get guess from user
                    current_guess = letter_guess()

                    # first check that the letter has not been guessed already
                    if current_guess not in guessed_letters:

                        # add guess to set of guessed letters
                        guessed_letters.add(current_guess)

                        # checks if the guessed letter is in the word and updates current word state
                        if current_guess in hangman_word:

                            print(
                                "#################################################")
                            print(f"Correct! {current_guess} is in the word.")

                            # find indices where the letter appears and add to list
                            letter_indices = []
                            for index, letter in enumerate(hangman_word):
                                if letter == current_guess:
                                    letter_indices.append(index)

                            # replace the correct underscore with the letter guessed and re-print
                            for index in letter_indices:
                                current_word_state = current_word_state[:index] + \
                                    hangman_word[index] + \
                                    current_word_state[index+1:]

                            # update guess counter and hangman state
                            guess_counter += 1
                            current_hangman_state = hangman_states[10 -
                                                                   lives_remaining]

                            print(f"You have {lives_remaining} lives left")
                            print(current_hangman_state)

                            break

                        # checks if the letter guessed is not in the word, updates hangman state and removes one from life counter
                        elif current_guess not in hangman_word:

                            # add guess to set of guessed letters
                            guessed_letters.add(current_guess)

                            print(
                                "#################################################")
                            print(
                                f"Unfortunately, {current_guess} is not in the word.")

                            guess_counter += 1
                            lives_remaining -= 1
                            current_hangman_state = hangman_states[10 -
                                                                   lives_remaining]

                            print(f"You have {lives_remaining} lives left")
                            print(current_hangman_state)

                            break

                    else:
                        print("""This letter has already been guessed \n """)

    else:
        print("GAME OVER -- ALL LIVES USED")
        print(hs_10)
        print(f"The word was: {hangman_word}")
        break
