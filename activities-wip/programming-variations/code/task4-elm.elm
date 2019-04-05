type Tree a
  = Empty
  | Node a (Tree a) (Tree a)
 
exampleTree : Tree Int
exampleTree = Node 4 (Node 1 Empty Empty) (Node 9 Empty Empty)

lookup : comparable -> Tree comparable -> Bool
lookup target tree =
  case tree of
    Empty -> False
    Node value left right ->
      if target < value then
        lookup target left
      else if target > value then
        lookup target right
      else
        True

-- Example evaluation        
-- > lookup 8 exampleTree  -- False
-- > lookup 9 exampleTree  -- True

-- Example evaluation after modification
-- > lookup 8 exampleTree 2  -- None
-- > lookup 9 exampleTree 1  -- Gold
-- > lookup 9 exampleTree 0  -- Basic
