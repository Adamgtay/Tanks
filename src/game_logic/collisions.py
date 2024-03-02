import math

# return true or flase for collisions between two objects


def isCollision(targetX, targetY, missileX, missileY, proximity):
    distance = math.sqrt((math.pow((targetX) - missileX, 2)) +
                         (math.pow((targetY) - missileY, 2)))
    if distance < proximity:
        return True
    else:
        return False
