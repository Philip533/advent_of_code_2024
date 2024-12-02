program one
  implicit none

  integer :: i
  integer, dimension(:,:), allocatable :: data

  allocate(data(1000,2))
  open(15, file="input.in")
  do i = 1, 1000
    read(15,*) data(i, :)
  end do

  ! Sort each dimension
  call bubble_sort(data(:,1))
  call bubble_sort(data(:,2))

  ! Sum up the distances
  print *, "Part 1 sum = ",sum(distances(data(:,1), data(:,2)))

  print *, "Part 2 sum = ", part2(data)
contains

  ! Using the first column and then searching for a match in column2
  integer function part2(array)
    integer, dimension(:,:) :: array
    integer                 :: i, j, key, count1, count2

    count1 = 0
    do i = 1, size(array,1)
      key = array(i, 1)

      count2 = 0
      do j = 1, size(array,1)
        if (array(j,2) == key) then
          count2 = count2 + 1
        end if
      end do
      count1 = count1 + key * count2
    end do
    part2 = count1
  end function

  ! Elemental function to vectorise the distance calculation
  elemental integer function distances(array1, array2)
    integer, intent(in) :: array1, array2
    distances = abs(array2 - array1)
  end function

  ! Take in 1D array and sort it
  subroutine bubble_sort(array)

    integer, dimension(:), intent(inout) :: array
    integer                              :: i
    integer                              :: temp
    logical                              :: sorted
    sorted = .false.

    ! We are done if no changes are performed
    do while (.not. sorted)

      ! Initialise to true
      sorted = .true.

      ! Loop over each element 
      do i = 1, size(array) - 1

        ! If wrong order, swap and say we are not sorted
        if (array(i) > array(i+1)) then
          temp = array(i+1)
          array(i+1) = array(i)
          array(i) = temp
          sorted = .false.
        end if
      end do
    end do
  end subroutine bubble_sort
end program one
