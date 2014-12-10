class Student
	attr_accessor :first_name, :last_name, :primary_phone_number
	# These are auto generated instance variable accessors without initial values

	def initialize
		# Does this once when instantiated
		@middle_name = "Rosales"
	end

	def introduction(target) # May omit parenthasis
		puts "Hi #{target}, I'm #{first_name}"
	end
end

danny = Student.new
danny.first_name = "Danny"
danny.introduction('Jeff')
puts danny.first_name
=begin
This wouldn't work with danny.middle_name even though it is an instance variable
because it has no accessor.
=end


randomNum = rand(5)
randNumString = randomNum.to_s
randomNumRange = rand(4..30)
pi = Math::PI # Accessing pi constant in the math class

3.times do
	puts pi
end

aRandArray = ['this', 'is', 'an', 5, [true, false]]
aRandArray.push 'one more item'
aRandArray.each do |item|
	puts item
end

=begin
Procs - you can pass blocks of code into and out of methods.
The following allows you to time how long any block of code takes to execute
without having to wrap said code in "startTime//duration then log duration"
every time you want to try it.
=end
def profile(descriptionOfBlock, &block) # must put & to store the code block
	startTime = Time.now

	block.call

	duration = Time.now - startTime

	puts descriptionOfBlock+' took:  '+duration.to_s+' seconds'
end

profile 'count to a million' do
	number = 0

	1000000.times do
		number = number + 1
	end
end

add_two = lambda { |number| number = number + 2 }
puts add_two.call(6) # A lambda is a stored code block, a 'block' isn't stored
