import React, { useState, useEffect } from 'react';
import { Box, Text, useColorModeValue, Center } from '@chakra-ui/react';

interface ServerStatusProps {
    checkInterval?: number;
}

const ServerStatus: React.FC<ServerStatusProps> = ({ checkInterval = 30000 }) => {
    const [isOnline, setIsOnline] = useState<boolean | null>(null);

    const onlineColor = useColorModeValue('limegreen', 'green');
    const offlineColor = useColorModeValue('crimson', 'red');
    const unknownColor = useColorModeValue('gray', 'gray');

    useEffect(() => {
        const checkServerStatus = async () => {
            try {
                const response = await fetch("https://makers-pc.monitor-liberty.ts.net/health");
                if (response.ok) {
                    setIsOnline(true);
                } else {
                    setIsOnline(false);
                }
            } catch (error) {
                setIsOnline(null);
            }
        };

        checkServerStatus();
        const intervalId = setInterval(checkServerStatus, checkInterval);

        return () => clearInterval(intervalId);
    }, [checkInterval]);

    const getStatusColor = () => {
        if (isOnline === null) return unknownColor;
        return isOnline ? onlineColor : offlineColor;
    };

    const getStatusText = () => {
        if (isOnline === null) return 'Unknown';
        return isOnline ? 'Online' : 'Offline';
    };

    return (
        <Center>
            <Box
                display="inline-flex"
                alignItems="center"
                borderRadius="full"
                bg={getStatusColor()}
                px={5}
                py={2}
                transition="all 0.3s ease-in-out"
                rounded='4px'
            >
                <Text fontSize="sm" fontWeight="bold" color='white'>
                    Server: {getStatusText()}
                </Text>
            </Box>
        </Center>
    );
};

export default ServerStatus;