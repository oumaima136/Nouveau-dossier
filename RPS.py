# The eiample function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[], play_order=[{
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            }]):
    if prev_play != '':
        opponent_history.append(prev_play)
    else:
        del opponent_history[:]
        del my_history[:]
        del play_order[:]
        play_order.append({
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            })
    ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
    inverse_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if len(my_history) < 1:
        played = "R"
        my_history.append(played)
    else:
        played = my_history[-1]
    
    two = ''.join(my_history[-2:])    
    if len(two) == 2:
        play_order[0][two] += 1

    potential_plays = [
        played + "R",
        played + "P",
        played + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]
    guess = ideal_response[prediction]

    if len(opponent_history) >= 5:   
      choice =''.join( ["R", "R", "P", "P", "S"]*2  )
      opponent_five = ''.join(opponent_history[-5:])
      indei = choice.find(opponent_five)
      if indei > -1:
        guess = inverse_response[choice[indei]]
        my_history.append(guess)
        return guess

    if len(opponent_history) >= 5:     
      hist =[ inverse_response[i] for i in my_history[-5:-1] ] 
      op_hist = opponent_history[-4:]

      if hist == op_hist:
        guess = ideal_response[my_history[-1]]
        my_history.append(guess)
        return guess
        
      if len(opponent_history) > 3:  
        if len(opponent_history) < 10:
            length = len(opponent_history)
        else:
            length = 10
          
        player4 = True
        for i in range(length-2):
            i = i + 1
            ten = my_history[-10-i:-i]
            most_frequent = max(set(ten), key=ten.count)
            if opponent_history[-i] != inverse_response[most_frequent]:
                player4 = False
        if player4:
            my_ten = my_history[-10:]
            most_frequent = max(set(my_ten), key=my_ten.count)
            response = ideal_response[most_frequent]
            my_history.append(response)
            return response

   
    
      
    my_history.append(guess)
    return guess
