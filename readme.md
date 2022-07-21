# The Game 
That's my simple version of Pong, the famous arcade game.

The objective of this game is simple; play with a friend and try to make the ball cross their line, while you try to defend yours.<br>
<br>
<img src="https://i.imgur.com/n4icWOD.png"  width="500" />

### Version 1.0 change log
```
💡 IDEA! - PvE gameplay
In the next update, I want try to make it possible to play this game versus the computer. Wait for it!
```


## Paddles
### Paddle Left

Move the paddle left by pressing "W", and "S" keys on your keyboard.

### Paddle Right

Move the paddle right by pressing "Up", and "Down" arrows on your keyboard.

## Ball
At the beginning of the game, or when some play scores, the ball will wait for the "Space" to be pressed on the keyboard to start the game.

Right before the ball starts rolling, a random direction will be chosen to follow forwards.

If the ball collides with the upper wall or bottom wall, the ball will " bounce" in the opposite direction on the Y axis. 
If the ball collides with the paddle, the ball will " bounce" in the opposite direction on the X axis.

When the ball crosses the paddle of some player, as they can't reach the wall, it's a score for the opposite player.

## Leveling  & Game over
As the player successfully defends the ball, bouncing it in the enemy's direction, the ball gets faster, making it harder to reach it.

When the game starts running, the players have to type how many rounds will end the game, also their names. 

When the scores of both players summed up reaches the value set at the start, the game ends, showing the player with a high score as the winner.

<img src="https://i.imgur.com/huq2C10.png"  width="500" />

## Reference
[Day 22 - 100 Days of Code](https://www.udemy.com/course/100-days-of-code/learn/lecture/20414753)
