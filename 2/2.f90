program two
  implicit none

  integer :: i, j

  type jagged_array
    integer, dimension(:), allocatable :: all_data
  end type 

  type(jagged_array), dimension(:), allocatable :: jagged
  type(jagged_array), dimension(:), allocatable :: difference
  integer, dimension(:), allocatable :: signs, array
  logical                :: safe
  integer                :: counter

  
  ! Read into the jagged array
  call read_input("input.in", jagged)

  counter = 0
  do i = 1, 1000
    array = (/ 0 /)
    ! print *, difference(i)%all_data
    call check_line_safe(jagged(i)%all_data, safe)
    ! print *, safe
    ! print *, safe, difference(i)%all_data

    if (safe) then
      counter = counter + 1
      cycle
    end if

    do j = 1, size(jagged(i)%all_data)
      array = (/ 0/)
      array = [(jagged(i)%all_data(:j-1)), jagged(i)%all_data(j+1:)]
      call check_line_safe(array, safe)
      if (safe) then
        print *, array
        counter = counter + 1
        exit
      end if
    end do
  end do

print *, "Part 1 solution = ", counter



contains

  ! Check if a line is safe
   subroutine check_line_safe(line, safe)

    integer, intent(in), dimension(:), allocatable :: line
    integer                                        :: sign
    integer                                        :: i, j 
    integer, dimension(:), allocatable             :: sign_array
    integer, dimension(:), allocatable             :: diff
    logical, intent(out)                           :: safe

    logical :: test , test2, test3
    test = .false.; test2=.false.; test3=.false.

    allocate(diff(size(line)-1))
    do j = 1, size(line) - 1
      diff(j) = line(j+1) - line(j)
    end do
    ! print *, line

    allocate(sign_array(size(diff)))

    do i = 1, size(diff)
      sign_array(i) = sign(1, diff(i))
    end do

    test = all(sign_array .eq. 1)
    test2 = all(abs(diff) <= 3)
    test3 = all(diff /= 0)
  
    ! print *, line
    if (test .and. test3) then
      if (test2) then
        safe = .true. 
        return
      end if
    end if

    test = all(sign_array .eq. -1)
  
    if (test .and. test3) then
      if (test2) then
        safe = .true. 
        return
      end if
    end if
    safe = .false.
    return

  end subroutine

  ! Take in the input file and return an array containing all of the columns
  subroutine read_input(input_file, full_data)
 
    character(len=*)      :: input_file
    character(len=256)    :: line
    integer, dimension(8) :: single_line
    integer :: i,j,k, istat, numcols

    type(jagged_array), dimension(:), allocatable :: full_data
    type(jagged_array), dimension(:), allocatable :: diff

    allocate(full_data(1000))
    open(15, file=adjustl(trim(input_file)))

    ! Go over each line and read into a character type
    do j = 1, 1000
      read(15,'(A)') line

      ! Try and read into an array to find the number of columns
      do i = 1, 10
        read(line,*,iostat=istat) single_line(1:i)
        if(istat == -1) then
          numcols = i
          exit
        end if
      end do

      ! Allocate the row and put the data in
      allocate(full_data(j)%all_data(numcols-1))
      full_data(j)%all_data = single_line(1:numcols-1)

    end do
  end subroutine
end program two
