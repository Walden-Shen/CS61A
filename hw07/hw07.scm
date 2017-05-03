(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; YOUR-CODE-HERE
  nil
)

(define (caddr s)
  ; YOUR-CODE-HERE
  nil
)

(define (sign x)
  ; YOUR-CODE-HERE
  nil
)

(define (square x) (* x x))

(define (pow b n)
  ; YOUR-CODE-HERE
  nil
)

(define (ordered? s)
  ; YOUR-CODE-HERE
  nil
)

(define (nodots s)
  ; YOUR-CODE-HERE
  nil
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ; YOUR-CODE-HERE
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ; YOUR-CODE-HERE
          (else nil)
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ; YOUR-CODE-HERE
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ; YOUR-CODE-HERE
          (else nil)
          ))


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ; YOUR-CODE-HERE
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

(define (as-list t)
    ; YOUR-CODE-HERE
    (else nil)
    )

