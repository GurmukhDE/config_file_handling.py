from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r"C:\Users\hp\Desktop\Data Engineering Python\configparser.ini")

brick_cost =config['raw_material']['brick_cost']

logger.info(f'{brick_cost}, type of brick_cost {type(brick_cost)}') 

"""#here in the output window, as we can see in the result the int values are stored in str always in INI file, 
so make sure whenever you work on that particular value are converting into an appropriate data type"""
#see line 27

def total_no_of_bricks(length, breadth, height):
    no_of_bricks_in_length_side = length*(height*2)
    total_no_of_bricks_in_length_side = no_of_bricks_in_length_side*2

    no_of_bricks_in_breadth_side = breadth*(height*2)
    total_no_of_bricks_in_breadth_side = no_of_bricks_in_breadth_side*2

    total_no_of_bricks = total_no_of_bricks_in_length_side + total_no_of_bricks_in_breadth_side

    return total_no_of_bricks

def total_cost_of_bricks(config):
    brick_cost = float(config['raw_material']['brick_cost'])#data type conversion from str to float
    total_no_of_bricks1 = total_no_of_bricks(15,15,10)

    final_cost = brick_cost*total_no_of_bricks1

    return final_cost

result = total_cost_of_bricks(config)

logger.info(f'the cost of total bricks for 1 room is:  {result}')

