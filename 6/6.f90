program six
  implicit none

  integer                                        :: num_lines, i, j, p1counter, loop_counter
  character(len=1), dimension(:,:), allocatable  :: array_plain, array_fill, array_obstruct
  character(len=1), dimension(:,:), allocatable  :: array_fill_trash
  integer, dimension(2)                          :: start_pos
  logical                                        :: is_loop

  !  Parse the input file
  num_lines = num_lines_in_file("input.in")
  array_plain = read_file("input.in", num_lines)
  start_pos = find_start_coords(array_plain)

  ! Do this once to get a path which we can later put obstructions on
  call perform_run(array_plain, start_pos,p1counter, array_fill, is_loop)
  print *, "Part 1 answer = ",p1counter

  ! Allocate everything
  allocate(array_obstruct(size(array_fill,1), size(array_fill,2)))
  allocate(array_fill_trash(size(array_fill,1), size(array_fill,2)))
  array_obstruct = array_plain

  ! Loop over the entire array
  do i = 1, size(array_fill,1)
    do j = 1, size(array_fill,2)

      ! Try an obstruction at each point along the path
      if (array_fill(i,j) == 'X') then

        ! Add obstruction
        array_obstruct(i,j) = '#'

        ! Do a run and find out if there's a closed loop or not
        call perform_run(array_obstruct, start_pos,p1counter, array_fill_trash, is_loop)

        ! Remove the obstruction and put it back to a blank space
        array_obstruct(i,j) = '.'

        ! If a loop has occurred, add it up
        if (is_loop) then
          loop_counter = loop_counter + 1
        end if
      end if
    end do
  end do
  print *, "Part 2 answer =", loop_counter
contains
  
  subroutine perform_run(array_in, start_pos, counter, array_out, loop)
    character(len=1), dimension(:,:), allocatable, intent(in)  :: array_in
    integer,          dimension(2),                intent(in)  :: start_pos
    integer,                                       intent(out) :: counter
    character(len=1), dimension(:,:), allocatable, intent(out) :: array_out
    logical,                                       intent(out) :: loop

    integer, dimension(2),                 :: position
    integer, dimension(:,:,:), allocatable :: direction_matrix
    character(len=1)                       :: direction

    loop = .false.
    allocate(array_out(size(array_in,1), size(array_in,2)))
    allocate(direction_matrix(size(array_in,1), size(array_in,2),4))
    
    ! Initiali conditions
    array_out = array_in
    direction = "u"
    position = start_pos
    counter = 1
    direction_matrix = -1

    do 
      ! Going up
      if(direction == "u") then

        if (position(1) == 1) then
          exit
        end if

        if(array_out(position(1), position(2)) == 'X' .and. direction_matrix(position(1),position(2),1) == 1) then
          loop = .true.
          exit
        end if

        ! visited this point and moved upwards
        direction_matrix(position(1), position(2), 1) = 1
        position = position + [-1,0]
        if (array_out(position(1), position(2)) == '.') then
          counter = counter + 1
          array_out(position(1), position(2)) = 'X'
        else if (array_out(position(1), position(2)) == '#') then
          position = position + [1,0]
          direction = "r"
        end if

      end if
      if(direction == "r") then

        ! Check if previously visited
        if(array_out(position(1), position(2)) == 'X' .and. direction_matrix(position(1),position(2),1) == 2) then
          loop = .true.
          exit
        end if

        if (position(2) == size(array_out,1)) then
          exit
        end if

        ! visited this point and moved upwards
        direction_matrix(position(1), position(2), 2) = 1
        position = position + [0,1]
        if (array_out(position(1), position(2)) == '.') then
          counter = counter + 1
          array_out(position(1), position(2)) = 'X'
        else if (array_out(position(1), position(2)) == '#') then
          position = position + [0,-1]
          direction = "d"
        end if

      end if

      if(direction == "d") then

        if(array_out(position(1), position(2)) == 'X' .and. direction_matrix(position(1),position(2),1) == 3) then
          loop = .true.
          exit
        end if

        if (position(1) == size(array_out,1)) then
          exit
        end if
        direction_matrix(position(1), position(2), 3) = 1
        position = position + [1,0]
        if (array_out(position(1), position(2)) == '.') then
          counter = counter + 1
          array_out(position(1), position(2)) = 'X'
        else if (array_out(position(1), position(2)) == '#') then
          position = position + [-1,0]
          direction = "l"
        end if
      end if

      if(direction == "l") then

        if(array_out(position(1), position(2)) == 'X' .and. direction_matrix(position(1),position(2),4) == 4) then
          loop = .true.
          exit
        end if

        if (position(2) == 1) then
          exit
        end if
        direction_matrix(position(1), position(2), 4) = 1
        position = position + [0,-1]
        if (array_out(position(1), position(2)) == '.') then
          counter = counter + 1
          array_out(position(1), position(2)) = 'X'
        else if (array_out(position(1), position(2)) == '#') then
          position = position + [0,1]
          direction = "u"
        end if
      end if
    end do

  end subroutine
  function find_start_coords(array) result(start_pos)
    implicit none

    integer :: i, j
    character(len=1), dimension(:,:), allocatable, intent(inout)  :: array
    integer, dimension(2) :: start_pos

    do i = 1, size(array,1)
      do j = 1, size(array,2)
        if (array(i,j) == "^") then
          start_pos = [i,j]
          array(i,j) = "X"
        end if
      end do
    end do
  end function
  function read_file(filename, num_lines) result(array)
    implicit none

    integer                                      :: num_lines, i, j
    character(len=*)                             :: filename
    character(len=255)                           :: line 
    character(len=1), dimension(:,:), allocatable  :: array

    open(15, file=filename)

    read(15, *) line
    allocate(array(num_lines, len(adjustl(trim(line)))))
    rewind(15)

    do i = 1, num_lines
      read(15,*) line
      do j = 1, len(adjustl(trim(line)))
        array(i, j) = line(j:j)
      end do
    end do
  end function read_file

  integer function num_lines_in_file(filename) result(num_lines)
    implicit none

    character(len=140) :: trash
    character(len=*)   :: filename
    integer            :: istat

    open(15, file=filename)

    num_lines = 0
    do
      read(15, *, iostat=istat) trash
      if(istat /= 0) exit
      num_lines = num_lines + 1
    end do
    close(15)
  end function num_lines_in_file
end program six
