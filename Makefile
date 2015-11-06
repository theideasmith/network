# project name (generate executable with this name)
TARGET   = networkgen


# change these to set the proper directories where each files shoould be
SRCDIR   = src
OBJDIR   = obj
BINDIR   = bin
INCLUDEDIR = include

SOURCES  := $(wildcard $(SRCDIR)/*.c)
INCLUDES := $(wildcard $(INCLUDEDIR)/*.h)
OBJECTS  := $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)
rm       = rm -f

BGET_HEADER=deps/bget/
BGET_OBJECTFILE=deps/bget/bget.o

CC       = gcc
# compiling flags here
CFLAGS   = -std=c99 -Wall -I$(BGET_HEADER)

LINKER   = gcc -o
# linking flags here
LFLAGS   = -Wall -I$(INCLUDES) -lm



$(BINDIR)/$(TARGET): $(OBJECTS)
	@$(LINKER) $@ $(LFLAGS) $(OBJECTS) $(BGET_OBJECTFILE)
	@echo "Linking complete!"

$(OBJECTS): $(OBJDIR)/%.o : $(SRCDIR)/%.c
	@$(CC) -I$(INCLUDEDIR) $(CFLAGS) -c $< -o $@
	@echo "Compiled "$<" successfully!"

.PHONEY: clean
clean:
	@$(rm) $(OBJECTS)
	@echo "Cleanup complete!"

.PHONEY: remove
remove: clean
	@$(rm) $(BINDIR)/$(TARGET)
	@echo "Executable removed!"
