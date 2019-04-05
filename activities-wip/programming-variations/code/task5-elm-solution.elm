type Tree a
  = Empty
  | Node a (Tree a) (Tree a)
  
exampleTree : Tree Int
exampleTree = Node 4 (Node 1 Empty Empty) (Node 9 Empty Empty)

type Membership
  = None | Basic | Gold

member : comparable -> Tree comparable -> Int -> Membership
member target tree maxDepth =
  case tree of
    Empty -> None
    Node value left right ->
      if target < value then
        member target left (maxDepth - 1)
      else if target > value then
        member target right (maxDepth - 1)
      else if maxDepth >= 0 then
        Gold
      else
        Basic
