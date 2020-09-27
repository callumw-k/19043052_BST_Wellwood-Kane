# Exercising model solution for Tutorial 7

import bst

sale = bst.BSTMap()

sale.add( 2, 'cup' )
sale.add( 1, 'brush' )
sale.add( 8, 'pot' )
sale.add( 5, 'hammer' )
sale.add( 3, 'mirror' )
sale.add( 9, 'table' )
sale.add( 6, 'hammer' )
sale.add( 12, 'mirror' )
sale.add( 50, 'table' )

print (sale.valueOf( 5 ))
print (sale.valuesOf( 2,50 ))
