#! /usr/bin/zsh
# =========================================1:-

# echo "Enter a character: "
# read input_char

# case "$input_char" in
#     [A-Z])
#         echo "You entered an Upper Case character."
#         ;;
#     [a-z])
#         echo "You entered a Lower Case character."
#         ;;
#     [0-9])
#         echo "You entered a Number."
#         ;;
#     *)
#         echo "You entered something else or multiple characters."
#         ;;
# esac

# =========================================2:-

# shopt -s extglob
# echo "Enter Name : "
# read name

# case $name in
#     +([A-Z])) 
# 	    echo "Capital Case "
# 	    ;;
#     +([a-z]))
# 	    echo "Small Case"
# 	    ;;
#     +([0-9]))
# 	    echo "Number"
# 	    ;;
#     +([A-Za-z]))
# 	    echo "mixed Character"
# 	    ;;
#     +([A-Za-z0-9]))
# 	    echo "mixed Character Number"
# 	    ;;
#     *)
# 	    echo "Not found"
#         ;;
# esac

# =========================================3:-

# for i in "$HOME"/*;
# do
#     if [ -f "$i" ] || [ -d "$i" ]; then
#         chmod u+x "$i"
#         echo "Added execute permission to: $i"
#     fi
# done

# =========================================4:-

# backup="$HOME/backup"

# for i in "$HOME"/*; do
#     if [ -f "$i" ]; then
#         cp "$i" "$backup/"
#         echo "Backed up: $i"
#     fi
# done

# =========================================5:-

# users=$(cat /etc/passwd | cut -d: -f1)
# for user in $users;
# do
#     mailx $user < letter
#     echo "mail to $user was sent"
# done

# =========================================6:-

# check_mail() {
#     mailbox_path="/var/mail/$(whoami)"
#     echo "New mail has arrived in $mailbox_path"
# }

# while true;
# do
#     check_mail
#     sleep 10
# done

# =========================================7:-

# typeset -i n1
# typeset -i n2
# n1=1
# n2=1
# while test $n1 -eq $n2
# do
#     n2=$n2+1
#     print $n1
#     if [ $n1 -gt $n2 ]
#     then
#         break
#     else
#         continue
#     fi
#     n1=$n1+1
#     print $n2
# done

# output = 1

# =========================================8:-

# select choice in "list content of dir" "list all content of dir" "Exit"
# do 
# 	case $REPLY in 
# 	1)	
#         ls
		
# 	;;
# 	2)	
#         ls -a
# 	;;
# 	3)	
# 		echo goodbye
# 		exit
# 	;;	
# 	*) 
# 	echo "invalid"
	
# 	esac
# done

# =========================================9:-

# echo "Enter the number of elements: "
# read num_elements

# if [[ ! "$num_elements" =~ ^[1-9][0-9]*$ ]]; then
#     echo "Invalid input."
#     exit
# fi

# my_array=()

# for ((i = 0; i < num_elements; i++)); 
# do
#     echo "Enter element $((i + 1)): "
#     read element
#     my_array+=("$element")
# done

# echo "Array elements:"
# for element in "${my_array[@]}"; do
#     echo "$element"
# done

# =========================================10:-


# numbers=()

# while true; 
# do
#     echo "Enter a number or enter anything else to exit: "
#     read input

#     if [[ ! "$input" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
#         break
#     fi

#     numbers+=("$input")
# done

# sum=0
# for number in "${numbers[@]}"; do
#     sum=$((sum + number))
# done

# average=$(($sum / ${#numbers[@]}))

# echo "Average of the entered numbers is: $average"

# =========================================11:-

# mysq() {
#     square=$(($1 * $1))
#     echo "The square of $1 is $square"
# }

# mysq 3