data Tree = Null 
          | Node
              { value :: Int
              , left :: Tree
              , right :: Tree
              }
          deriving Show

insert :: Tree -> Int -> Tree
insert Null x = Node x Null Null
insert node x
    | x < value node = node { left = insert (left node) x }
    | x > value node = node { right = insert (right node) x }
    | otherwise      = node

printInorder :: Tree -> IO ()
printInorder Null = return ()
printInorder tree = do
    printInorder $ left tree
    putStr . show $ value tree
    putStr " - "
    printInorder $ right tree

main :: IO ()
main = printInorder $ foldl insert Null [5, 4, 2, 8]
