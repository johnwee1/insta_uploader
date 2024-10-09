import { SetStateAction, useState, useEffect } from 'react';
import { ChakraProvider, Box, VStack, HStack, Heading, Input, Textarea, Button, useToast } from '@chakra-ui/react';

const SimpleForm = () => {
    // Manage form state
    const [name, setName] = useState('');
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);
    const toast = useToast();

    // Handle input changes for name
    const handleNameChange = (e: { target: { value: SetStateAction<string>; }; }) => {
        setName(e.target.value);
    };

    // Handle input changes for message
    const handleMessageChange = (e: { target: { value: SetStateAction<string>; }; }) => {
        setMessage(e.target.value);
    };

    // Handle form submission
    const handleSubmit = async (e: { preventDefault: () => void; }) => {
        e.preventDefault();
        if (loading) return;
        setLoading(true);

        const formData = {
            name,
            message
        };

        try {
            const response = await fetch('https://makers-pc.monitor-liberty.ts.net/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                toast({
                    title: "Form submitted",
                    description: "We've received your message!",
                    status: "success",
                    duration: 3000,
                    isClosable: true,
                });
                setName('');
                setMessage('');
            } else {
                throw new Error('Failed to submit form');
            }
        } catch (error) {
            toast({
                title: "Error",
                description: "Error occurred. Maybe your message was malicious! I'm a lazy coder, so that's up to you to figure out.",
                status: "error",
                duration: 3000,
                isClosable: true,
            });
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (loading) {
            toast({
                title: "Loading",
                description: "Please wait while we process your request...",
                status: "info",
                duration: null,
                isClosable: false,
            });
        } else {
            toast.closeAll();
        }
    }, [loading, toast]);

    return (
        <ChakraProvider>
            <Box
                minHeight="30vh"
                bg="gray.100"
                py={12}
                textAlign="center"
            >
                <VStack
                    spacing={8}
                    maxWidth="600px"
                    margin="auto"
                    align="center"
                    bg="white"
                    p={8}
                    borderRadius="md"
                    boxShadow="lg"
                >
                    <Heading as="h1" size="xl" textAlign="center">
                        REPRIVY RELOADED 💌
                    </Heading>
                    <Box as="form" onSubmit={handleSubmit} style={{ width: '100%' }}>
                        <VStack spacing={4} align="center">
                            {/* Name input */}
                            <HStack width="100%" justify="center">
                                <Input
                                    placeholder="Your Batch and Name (eg R13)"
                                    size="lg"
                                    value={name}
                                    onChange={handleNameChange}
                                    width="80%"
                                />
                            </HStack>

                            {/* Message textarea */}
                            <HStack width="100%" justify="center">
                                <Textarea
                                    placeholder="Your Message"
                                    size="lg"
                                    value={message}
                                    onChange={handleMessageChange}
                                    width="80%"
                                />
                            </HStack>

                            {/* Submit button */}
                            <Button type="submit" colorScheme="blue" size="lg" width="40%">
                                Submit
                            </Button>
                        </VStack>
                    </Box>
                </VStack>
            </Box>
        </ChakraProvider>
    );
};

export default SimpleForm;



